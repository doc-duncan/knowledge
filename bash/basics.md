### Bash Basics

#### `grep`
**purpose** string search using regex
```bash
# finds all instances of "world"
echo "hello world, today is world day!" | grep -o "world" # output = "world world"
# -o is used to just get the instances that match the regex, not the entire line
```

#### `sed`
**purpose** string replacement/transformation
```bash
# substitutes all instances of "hello" with "world"
echo "hello world" | sed "s/hello/world/g" # output = "world world"
# g means 'global' - which is used to substitute all instances
# by default grep only substitutes the first instance found on each line
```

#### line continuation
```bash
# no space, new line or tab after "\"
echo "this is \
a multiline \
command"
```