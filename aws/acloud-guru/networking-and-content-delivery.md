## CloudFront

1. What are the two types of CloudFront distributions and what are they used for?
    1. Web - used for basic web content
    2. RTMP - used for streaming
2. What is invalidating the CloudFront cache and is it free?
    1. Invalidating the cache pushes new changes to the CloudFront cache. There is a small fee for invalidating.
3. When would you use a CloudFront cookie vs. a signed url.
    1. A cookie should be used for accessing multiple objects.
    2. A signed url should be used for a single object.
4. What can't you use with an RTMP distribution?
    1. cookies
5. Draw a diagram showing the retrieval of a CloudFront signed url or cookie.
    ![cloudfront-url-cookies](/aws/acloud-guru/img/cloudfront-url-cookies.jpg)

