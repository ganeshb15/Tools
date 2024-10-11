# SRT File Generator Tool

## Overview
This tool allows you to generate an SRT (SubRip Subtitle) file from two input files:
- A **CSV file** containing subtitles.
- A **Label file** containing time information.

### Input File Formats:
1. **CSV File**: Contains subtitles in the format: `index,subtitle`.
   - Example `1.csv`:
     ```
     1,ದಿ. ಶ್ರೀ. ಹೊಸ್ತೋಟ  ಮಂಜುನಾಥ  ಭಾಗ್ವತ .
     2,ಯಕ್ಷಗಾನದ ಆರಾಧಕ , ಸಂಶೋಧಕ, ಕವಿ ,. ಸಾಹಿತ್ಯಕಾರ.
     ```

2. **Label File**: Contains start and stop times for each subtitle in the format: `start_time_in_seconds stop_time_in_seconds subtitle_index`.
   - Example `Labetrack.txt`:
     ```
     411.750986	706.944770	1
     912.186801	1277.061521	2
     ```
   - Where:
     - First column: Start time (in seconds).
     - Second column: Stop time (in seconds).
     - Third column: Index corresponding to the CSV subtitle.

## How to Use

1. **Prepare the Input Files**:
   - Create a **CSV file** with your subtitles. Each line should follow the format `index,subtitle`, where `index` corresponds to the label index, and `subtitle` is the subtitle text.
   - Create a **Label file** with start and stop times. Each line should contain `start_time stop_time index`, where `start_time` and `stop_time` are in seconds, and `index` refers to the subtitle index from the CSV file.

2. **Run the Tool**:
   - When you run the script, a window will appear with buttons for selecting files.
     - Click **Label File** and select your label file (`Labetrack.txt`).
     - Click **CSV File** and select your CSV file (`1.csv`).
   - After both files are selected, click **Run** to generate the SRT file.

3. **Output File**:
   - The tool will generate an `Output.srt` file in the same directory as your CSV file.
   - The SRT file will be formatted as follows:
     ```
     1
     00:06:51 --> 00:11:46
     ದಿ. ಶ್ರೀ. ಹೊಸ್ತೋಟ  ಮಂಜುನಾಥ  ಭಾಗ್ವತ .

     2
     00:15:12 --> 00:21:17
     ಯಕ್ಷಗಾನದ ಆರಾಧಕ , ಸಂಶೋಧಕ, ಕವಿ ,. ಸಾಹಿತ್ಯಕಾರ.
     ```

### Step-by-Step Recap:
1. Open the tool window.
2. Select the **Label file** (`Labetrack.txt`) and **CSV file** (`1.csv`) using the provided buttons.
3. Click **Run** to generate the SRT file.

### Confirmation:
- After the SRT file is created, a message box will display **"Done"**, indicating that the process is complete.
- The generated SRT file (`Output.srt`) will be saved in the same folder as the CSV file.

