## Protocol Buffers

*Disclaimer: info. for this page was sourced from [here](https://developers.google.com/protocol-buffers/docs/gotutorial)*

### Introduction - Why Protocol Buffers?
Because of the microservice architecture and ecosystem today, there are many modular systems that need to exchange data back and forth. These systems need to agree on a contract of what this data will look like and then they need to worry about serialization and deserialization. You might say, well why can't we just put an xml or json doc out there and every system must conform to that structure? This is completely valid, but the problem with this is that serialization and deserialization can be time and space intensive. Secondly, on both sides you have to use disparate methods/functions for navigating and updating the data at hand. **Protocol buffers solve these problems by doing the following:**

1. Serialization is done to a minimal byte encoding, which makes the object small
2. Compilation of the `.proto` file for your language specific needs allows for code generation of all getters, setters and helper methods, so it is easy to work with the data

### Tutorial
So let's get started on creating a simple flow. Let's say that we have service "A" that needs to send data to service "B". More specifically, we want to send user data for a person that has recently signed up for service "A". We need the first and last names of the user and an email address to be sent to service "B".

We start by creating a `sample.proto` file, which holds our data definitions. We can compile this file into many language specific helper entities (classes, functions, structs...).

```protobuf
// this is the version of protocol buffer syntax you wish to use
syntax = "proto3";

// this is a protocol buffer package - specific to PB, and not related to Go or anything else
// used as a logical grouping
package tutorial;

// IF USING GO YOU WILL NEED THIS, IT DEFINES THE IMPORT PATH FOR THE GENERATED GO CODE
// all directories not existing will be made with this line
option go_package = "example.com/sample/samplepb"

...
```

Now that the boilerplate is out of the way we can add some structured data to our file. We will add a `User` definition as a `message` to our `.proto` file. `message` is the type used by the protocol to describe a logical grouping of data. Within a given `message` we define `fields`, similar to a JSON object. Each `field` is assigned a number, which serves as an identifier, and **not** and actual value, for that field. These identifiers are used by the protocol for encoding and decoding the data.

```protobuf
...

message User {
    string first_name = 1;
    string last_name = 2;
    string email = 3;
}
```

We can then compile our `.proto` definition into language specific entities (classes, functions, structs...) by using the [protoc compiler](https://developers.google.com/protocol-buffers/docs/downloads). Some languages also require a language package like [Go](https://pkg.go.dev/google.golang.org/protobuf/cmd/protoc-gen-go).

Once you have the above dependencies installed, you can run the following (this will build a Go specific object).

`protoc --go_out=./ sample.proto`

The above command tells `protoc` to compile the `sample.proto` file as `Go` entities and place it/them into the current directory. This will specifically result in a `sample.pb.go` file, which will have a `User` struct defined and all corresponding getters, setters, encoders and more.

You can then import the generated code into your source code for service "A" to build a `User` object.

```Go
...
// service A
import ...

user := &User{
    FirstName: "John"
    LastName: "Doe"
    Email: "john.doe@icloud.com"
}

...
```

The whole purpose of these protocol buffers is to be able to share and ingest data easily though! If I wanted a `User` struct I would have just made one. So lets encode the data, write it to a file and then have service "B" pick it up.

```Go
...
// service A
import ...

user := &User{
    FirstName: "John"
    LastName: "Doe"
    Email: "john.doe@icloud.com"
}

// Write the user to disk.
out, err := proto.Marshal(book)
if err != nil {
        fmt.Println("Failed to encode user:", err)
}
if err := ioutil.WriteFile("output", out, 0644); err != nil {
        fmt.Println("Failed to write user:", err)
}
...
```

After performing the above operations in service "A" we will be left with a file named `output` that will have the encoded data in it. The true beauty of protocol buffers is that service "B" could then be written in Python, have the compiled `.proto` as a Python object and ingest the `output` file encoding with no problem, like so.

```Python
...
# This is the compiled Python object
import user_pb

# Init. class to load with data
user = user_pb.User()
# Read in existing user from output file
f = open("output", "rb")
# Use PB methods for decoding
user.ParseFromString(f.read())
f.close()

# Access attributes
print(user.first_name)
...
```
