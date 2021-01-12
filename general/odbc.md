## ODBC - Open Database Connectivity

*Disclaimer: info. for this page was sourced from [here](https://www.youtube.com/watch?v=VkMXJvaWeTE)*

#### General
- ODBC is an API for accessing database systems, which is often referred to as **drivers**
- Each database will have its own driver - **it is not dependent upon the application**

#### Why use ODBC?
- ODBC allows for language agnostic connections to a database
- This means the vendor only needs to develop a single driver that will allow all types of connections
- Sometimes you will need to install other packages like pyodbc to interface with that driver
depending on the language so you do not have to reinvent the wheel

#### Installing ODBC Drivers
- More often than not you need to install the driver from the vendor site
- **It is very important that you install the 32 or 64 bit version, depending on the application
interfacing with the driver (Python, R...) and not the entire system itself**
