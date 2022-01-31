# Go Proxy and Checksum DB
As of Go 1.13, Go Modules are the standard. Modules leverages both the Go proxy and Checksum Database for efficiently and securely fetching packages.

## Go Proxy
There is a Go environment variable called `GOPROXY` that you can check out on your environment using the command `go env`. This environment variable tells Go where to download modules from. Often times it is a comma separated list that ends in `direct`. Something like `GOPROXY="https://proxy.golang.org,direct"` is standard. This tells Go to reach out to `https://proxy.golang.org` for all modules first and if it can't find them there, then go straight to the VCS system (`direct`). **One caveat to the proxy is that all modules must be publicly accessible. This is not the case **