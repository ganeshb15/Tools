function CaptureOutput


    [ModelName ModelPath] = uigetfile('*.slx', 'Select Test Model');
    fidx = strfind(ModelName, '.');
    ModelName = ModelName(1:fidx-1);
    load_system(ModelName);
    OutputPorts = find_system(ModelName, 'SearchDepth', 2, 'BlockType', 'Outport');
    InputPorts = find_system(ModelName, 'SearchDepth', 2, 'BlockType', 'Inport');
    OpNames = get_param(find_system(ModelName, 'SearchDepth', 2, 'BlockType', 'Outport'), 'Name');
    IpNames= get_param(find_system(ModelName, 'SearchDepth', 2, 'BlockType', 'Inport'), 'Name');
    %Remove Inputs "EVENT OR SCHED" from the inputs list
    SchdEvnts = strncmp(IpNames, 'Sched', 5) | strncmp(IpNames, 'Event', 5);
    IpNames(SchdEvnts) = [];
    IOPorts = [OutputPorts; InputPorts];
    IOPorthandles = get_param(IOPorts, 'handle');
    for i = 1:1:length(IOPorthandles)
        IOPortData.(get_param(IOPorthandles{i}, 'Name')) = get(IOPorthandles{i});
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for onp = 1:1:length(OpNames)
        if( ~(strncmp(IpNames,'Event',5) | strncmp(IpNames,'Sched',5)))
            ToWsBlkPath = [eval(['IOPortData.' OpNames{onp} '.Parent']) '/ToWS' OpNames{onp}];
            ToWsBlkPos = eval(['IOPortData.' OpNames{onp} '.Position']);
            ToWsBlkPos(1) = ToWsBlkPos(1) + 50; ToWsBlkPos(3) = ToWsBlkPos(3) + 50;
            ToWsBlkPos(2) = ToWsBlkPos(2) - 20; ToWsBlkPos(4) = ToWsBlkPos(4) - 20;
            if isempty(find_system(ModelName, 'BlockType', 'ToWorkspace', 'VariableName', OpNames{onp}))               %CHECK IF THE TOWS BLOCK IS ALREADY PRESENT
                add_block('simulink/Sinks/To Workspace',ToWsBlkPath, 'Position', ToWsBlkPos,'ShowName', 'off', 'VariableName', OpNames{onp}, 'SaveFormat', 'StructureWithTime');
                SrcPath = [get_param(eval(['IOPortData.' OpNames{onp} '.PortConnectivity.SrcBlock']), 'Name') '/' ...
                    num2str(eval(['IOPortData.' OpNames{onp} '.PortConnectivity.SrcPort'])+ 1)];
                add_line(eval(['IOPortData.' OpNames{onp} '.Parent']), SrcPath, ['ToWS' OpNames{onp}, '/1'], 'autorouting', 'on');
            end
        end
    end
    %%
    SignalBuilderName = find_system(ModelName, 'SearchDepth', 1, 'MaskType', 'Sigbuilder block');
    %[time,data] = signalbuilder(SignalBuilderName{1});
    [time,data,signames] = signalbuilder(SignalBuilderName{1});
    data1=[];
    for i=1:length(data)
        data1=horzcat(data1,data{i}');
    end
    data1=vertcat(signames,num2cell(data1));
    time1=vertcat('___t___',num2cell(time{1}'));
    SimTime = {'Simulation Time','Output File Name CSV'};
    SimTime = inputdlg(SimTime);
    sim(ModelName,str2num(SimTime{1}))
    OpNames1=unique(OpNames);
    OutputValue=[];
    for i=1:length(OpNames1)
        t=eval([OpNames1{i} '.signals.values']);
        OutputValue=horzcat(OutputValue,t);
    end

    OutputValue1=vertcat(OpNames1',num2cell(OutputValue));
    FinalOut=horzcat(data1,time1,OutputValue1);
    xlswrite([SimTime{2} '.csv'],FinalOut);
end