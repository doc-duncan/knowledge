## Go <!-- omit in toc -->
This reference was made while following along with the O'Reilly *Learning Go* book - I owe all notes in this document
to it.

> Idiomatic Go values comprehensibility over conciseness.
The above is a quote from the book that pretty much sums up how Go is structured.

> Go programs compile to a single binary and do not require any additional software to be installed in order to run
> them. Install the Go development tools only on computers that build Go programs.

- [Structuring, Building and Running](#structuring-building-and-running)
- [Types](#types)
  - [Boolean](#boolean)
  - [Integer](#integer)
  - [Float](#float)
  - [Complex](#complex)
  - [String](#string)
  - [Rune](#rune)
  - [Type Conversion](#type-conversion)
- [Declaring/Initializing Variables](#declaringinitializing-variables)
- [Const](#const)

### Structuring, Building and Running
 **If you just want to test out a Go program or script quickly then use `go run <your-program.go>`.** This will build a
temporary binary, run it and then delete the binary (great for quick POC testing).

**Use `go build <your-program-or-package>` to build your source into a binary of the same name.** If you provide the
`-o` flag you can name the binary that is produced.

To install third party Go programs you can use the `go install` command. This command will download the source and
compile it under `$GOPATH/bin`. Therefore, be sure to add `$GOPATH/bin` to your `PATH` so you can execute these
tools. `go install` actually targets the source and builds the binary on the fly, however, if you want to distribute
your program as a prebuilt binary for download then that is perfectly fine.

### Types
Listed below are the Go types and their corresponding **"zero value"**. A zero value is the value
that the variable defaults to if it is not initially set.

#### Boolean
zero value: `false`

keywords:
- `bool`

#### Integer
zero value: `0`

keywords:
- `int8 \\ -128 to 127 range (signed ex. 01111111 = 127)`
- `int16 \\ -32768 to 32767`
- `int32 \\ -2147483648 to 2147483647`
- `int64 \\ -9223372036854775808 to 9223372036854775807`
- `uint8 \\ 0 to 255`
- `uint16 \\ 0 to 65535`
- `uint32 \\ 0 to 4294967295`
- `uint64 \\ 0 to 18446744073709551615`


*`int` and `uint` default to `(u)int32` or `(u)int64` depending on the architecture of the machine. Secondly, `byte`
is simply an alias for `uint8`.*

#### Float
zero value: `0`

keywords:
- `float32`
- `float64`

**As in many other languages, floats in Go cannot be relied upon to be exactly precise. Therefore, do not assert
equality between floating point numbers. Instead specify an acceptable tolerance and check the difference of the
floats. More often than not you shouldn't be using them.**

#### Complex
zero value: `0 real` and `0 imaginary`

keywords: 
- `complex64`
- `complex128`

*Yes, Go does have complex numbers, but they are scarcely used so it is just beneficial to know that they exist.
Because of this, we won't dive into any detail around them.*

#### String
zero value: `""`

keywords:
- `string`

#### Rune
zero value: `''`

keywords:
- `rune`

*A rune represents a single character, and is actually just an alias for `int32`*

#### Type Conversion
Go values being explicit. Therefore, all type conversion is explicit to avoid having to remember automatic conversion
rules. For this reason, you must always align your types of variables prior to an action between them.

For example:

```go
var x int = 3
var y float64 = 3.0
var z float64 = float64(x) + y 
```

There is also no "truthiness" in Go. Nothing can be interpreted as a `bool` except a `bool`.

### Declaring/Initializing Variables
There are multiple ways in Go to declare and initialize variables. Let's start from the top...

1. `var x int` will create x with its zero value
2. `var x int = 10` is the most verbose way of initializing
3. `var x = 10` assumes x will be of type `int`
4. `var x, y = 10, "hello"` initializing multiple vars
5. variable declearation block
  ```go
   var (
    x int
    y = 3
    j = "hi"
   )
   ```
6. `x := 3` The `:=` initialization can be used only within functions, but is nice shorthand. *Note: you can use `:=`
to initialize multiple variables, but at least one of the variables needs to be new. Secondly, please read the
"Shadowing Variables" section to learn about some pitfalls of `:=` that can lead to subtle bugs.* 

### Const
You can declare constants in similar ways to `var`:
```go
const d int64 = 90

const (
  hello = "hello"
  world = "world"
)
```
**However, it is important to note that `const`s can only be set to values that the compiler can determine at compile
time.**

Lastly, constants can be explicitly typed or untyped. For example:

```go
// By making x untyped below, we are able to set multiple different typed vars to it
const x = 10

var a int = x
var b float64 = x
var c byte = x

// In comparison to the typed constant below, which can only be ever assigned to int types
const y int = 10
```