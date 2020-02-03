Step 1 : aws dynamodb scan --table-name TABLE_NAME > export.json (display complete records of the table and display total records also).

step 2 : aws dynamodb scan --table-name TABLE_NAME --query Items[] > data.json (display records of table rest of unwanted parts of json will be removed).

step 3 : provide file path of test case which under test package and run the test case.

step 4. change table name in constant file ie., which table all records want to push.

step 5. wait untill successfull or error records will be display in console.

step 6. check in aws console whether records are getting reflected or not.