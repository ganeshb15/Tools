function t4 = ggcb
	openModels = find_system('SearchDepth', 0);
	t1=gcb;
	t2=strsplit(t1,'/');
	idxx=strcmp(openModels,t2{1});
	idx12=find(idxx==0);
	openModels1=openModels(idx12);
	t4={};
	for i=1:length(openModels1)
    		mdlrefs = find_system(openModels1{i},'LookUnderMasks','on','FollowLinks','on','BlockType','ModelReference');
    		mdls = get_param(mdlrefs,'ModelName');

    		idx=strcmp(t2{1},mdls);
    		idx11=find(idx==1);
    		t3=mdlrefs(idx11);

		if(~isempty(t3))
        		t4=[t3{1} '/' t1];
        		break;

    		end
	end

	if(isempty(t4))
    		t4=gcb;
	end
end
