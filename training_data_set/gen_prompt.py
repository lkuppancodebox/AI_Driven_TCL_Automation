import pandas as pd
import json
import ast  # To safely evaluate dictionary strings

test_block_template = '''
######### Sample Test Step ###############

set subTestTitle "Configure DUT-A"
result_h2 "$subTestTitle" ;# Print test step title
report_start_test "$subTest" ;# Test step start block
Login $DUT1_CONNECT

  SendACmd        "clear fdb"
  SendACmd        "clear iparp"
  SendACmd        "clear counters"

report_end_test ;# Test step end block
'''

test_script_template = '''
######### Test Script Template ###############

proc "Test case id from use case" {} {

set testcase_id "test_case_id is same as proc name"
set TestCaseTitle "$testcase_id: Test case Title or test objective from use case"

# ----- Declare global variables first
global DUT1_CONNECT
global DUT2_CONNECT
global DUTs_info

set fd_res [open_result_file "$testcase_id"]
set time1 [clock seconds]

  ### Test case start block
  result_h1 "$TestCaseTitle"
  report_start_test "$TestCaseTitle"

    ### test step block 1
    ### test step block 2
    ### test step block 3
    ### so on...

  set time2 [clock seconds]
  result_p "*** Time for $testcase_id = [expr $time2-$time1] secs\n\n"
  close_result_file
  report_end_test
  ### Test case end block
}
'''

def tclLib2Json(csv_file='/content/drive/MyDrive/Colab Notebooks/training_data_set/lib.csv'):
    # Read CSV
    df = pd.read_csv(csv_file)

    # Process tcl_arguments (convert comma-separated string to list)
    df['tcl_arguments'] = df['tcl_arguments'].apply(lambda x: x.split(", ") if pd.notna(x) else [])

    # Process mandatory_arguments (convert string dict to actual dict)
    df['mandatory_arguments'] = df['mandatory_arguments'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else {})

    # Process optional_arguments (convert string dict to actual dict)
    df['optional_arguments'] = df['optional_arguments'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else {})

    # Convert DataFrame to JSON
    json_data = df.to_dict(orient="records")

    return json_data
  

def generate_prompt(query, tcl_lib_json_dataset, test_case = test_script_template, test_step = test_block_template) :

  # Example usage
  prompt = f'''
  **Use case: {query} **

  Generate TCL Script for the above Use case based on following available tcl library.

  Available TCL Procedures :
  { json.dumps(tcl_lib_json_dataset, indent=2) }

  # Each test step should be in the format below:
  # Use the same indendation method for your script

  {test_step}


  # Use the test case template below to insert all generated test steps.
  # The `proc` name and `testcase_id` **must** use the **test case ID from the "Use case:"**. Do **not** generate a new test case ID—strictly use the given one.

  {test_case}
  '''
  return prompt

  


