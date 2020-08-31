# InfosecCodePrompt
Test Case Steps:

1. Attempt to create account with no email, expected error message
2. Attempt to create account with invalid email, expected failed field validation and error message on submission
3. Attempt to create account with valid email, expect to proceed to next page upon submission, verify provided email is in the info email field
4. Attempt to register with no required fields entered, expected error message
5. Attempt to register with some but not all required fields filled, expect error message
6. Attempt to register with some non-required fields filled and no required fields, expect error message
7. Attempt to enter a number into first name field then click out of the field, expect failed field validation
8. Attempt to enter a string with special characters (/\[](){}@&$) into first name field then click out of the field, expect failed field validation
9. Attempt to enter a long string into first name field then click out of the field, expect successful field validation
10. Attempt to enter a normal length string into first name field then click out of the field, expect successful field validation and verify this value is auto filled into the address first name field
11. Attempt to enter a string into the last name field, verify this value is auto filled into the address last name field
12. Attempt to enter a string of fewer than five characters into the password field then click out of the field, expect failed field validation
13. Attempt to enter a string of five or more characters containing any of the above from 7-9 into the password field then click out of the field, expect successful field validation
14. Attempt to enter a non-mumeric string into the ZipCode, expect error upon submitting
15. Attempt to enter a numeric string of under 5 characters, expect error upon submit
16. Attempt to enter a numeric string of over 5 characters, expect error upon submit
17. Attempt to enter a numeric string of exactly 5 characters, expect no zipcode error upon submit
18. Attempt to enter a non-numeric string into the mobile phone number field, expect phone number error
19. Attempt to enter a numeric string into the mobile phone number field, expect no error for phone number
20. Attempt to complete form with all required fields properly filled in, expect no errors, taken to the My Account Page

Notes about site functionality:

* Every field in the Your Address section has no field based validation like in the Your Personal Information section
* Can enter all numbers in City field
* Can enter any number of digits into phone number field
* Inconsistent naming of ids and classes (some are camelCase, some use an underscore)

Future improvements to test:
* Proper wait conditions
* Visual debugger integration
* More comprehensive validation functions
* Creatation of getter/setter for fields

Change Log:
* August 27, 2020 - File creatation and test case steps written
* August 28, 2020 - First ten steps of test written, added notes about the test site's functionality and structure
* August 29, 2020 - Final ten steps of test written, added section on future improvments to the test
* August 30, 2020 - Create page objects for test use
* August 31, 2020 - Creates version 2 of test using page objects
