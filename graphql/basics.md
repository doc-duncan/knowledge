### GraphQL

> What is GraphQL?
GraphQL is both a query language and a service that allows for consistent data access via your API.

You can look at GraphQL as a layer on top of your API that is in charge of grouping and filtering the data.

For example, let's say you had an API that described the 100 Acre Wood.

Without GraphQL you may have an endpoint such as `/getInhabitants`, which would return the `name` and `address` of each
person in the wood.

Now let's say a user didn't need the address (a very trivial example, but you get the point). If you put GraphQL on top
of the API a a user could specify a query like the following and receive just the names.

```graphql
{
    Inhabitant {
        name
    }
}
```

Then on the server side you would have a type definition that would look like the following:
```graphql
type Inhabitant {
    name: String
    address: String
}
```

You would then have a resolver function on the server that would call `/getInhabitants` and return the object to
GraphQL, which would do the filtering.