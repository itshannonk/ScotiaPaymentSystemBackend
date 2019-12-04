# Scotiabank Payment System Backend
This is the backend for an Android app created in CSC207 in collaboration with Scotiabank.

## Motivation
As of now, there are a variety of ways that small business (eg. a convenience store), can pay for good delivered by their suppliers.
The plethora of options often runs into documentation problems as it is hard to keep track of payments and invoices in this un-standardized system.
What we have built is a business-to-business platform that allows user to issues, track and pay invoices.
In this repository, you will find cloud functions that create, manage and edit data concerning the users of the app.

## Tech/frameworks used
We hosted the functions in main.py as cloud functions on Google Cloud Platform.
Additionally, we used the firebase and pyrebase Python packages to make calls to the our Firebase real-time database.

## Features
We have completely separated the cloud functions and http endpoints from the database invocations.
What this means is that these functions are easily extendable and can still work if you wish to implement another type of database.

Furthermore, we have provided various implementations of similar http requests.
For example, if a clients wishes to access a list of invoices, they can get it returned to them as a comma separated list or a a json object.
This gives clients a variety of implementation options.

## Licence

   Copyright 2019 © [!WHAT IS OUR GROUP NAME!]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
