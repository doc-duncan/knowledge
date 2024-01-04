## Appium :iphone: <!-- omit from toc -->

*Disclaimer: The information presented in this document was sourced with gratitude from various people that are much
more knowledgeable than me on this topic. I have done my best to link to these sources in-place, but credit is given
to all in the [reference section below](#References).*

### Table of Contents <!-- omit from toc -->
- [Overview](#overview)
- [How Does Appium Work?](#how-does-appium-work)
- [References](#references)

### Overview
I'm sure you could have guessed this, but this document goes over [Appium][Appium]. The official sites of Appium
and Selenium describe the reason for their existence in a more up-to-date way I'm sure, but for my future self:
1. Appium and Selenium facilitate the UI automation of applications backed by various platforms and/or browsers.
2. They do the above in a way that allows a single implementation (an automated test for example) to run against
numerous platforms without a change in the logic.

### How Does Appium Work?
To be honest, I can't even come close to matching the [explanation provided by the Appium team][How Does Appium Work?].
However, again for my future self, below are notes on the referenced explanation...

Ridiculously high level flow:
1. You write an automation script or test in the language of your choosing using the [Appium libraries][Appium Clients].
2. When the script is run the language specific calls are each transformed into a JSON object.
3. Each JSON object is the body of an individual HTTP call to the Appium server ("Browser Driver" in Selenium's case),
which implements the [WebDriver Specification][WebDriver Specification].
4. The Appium server hands the data off to a "driver" that implements an "Appium-like WebDriver specification".
5. This platform specific driver handles the interaction with the platform using vendor automation frameworks.

Honestly though, please read the official explanation above, it is unmatched.

### References
* [Appium](https://appium.io/docs/en/2.4/)
* [How Does Appium Work?](https://appium.io/docs/en/2.4/intro/appium/)
* [Appium Clients](https://appium.io/docs/en/2.4/ecosystem/clients/)
* [WebDriver Specification](https://w3c.github.io/webdriver/webdriver-spec.html)

<!-- links (should match above) -->
[Appium]: https://appium.io/docs/en/2.4/
[How Does Appium Work?]: https://appium.io/docs/en/2.4/intro/appium/
[Appium Clients]: https://appium.io/docs/en/2.4/ecosystem/clients/
[WebDriver Specification]: https://w3c.github.io/webdriver/webdriver-spec.html