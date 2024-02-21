## Assignment

[Article used ](https://portswigger.net/research/http2)
### What was wrong with HTTP2
The vulnerabilities in HTTP/2 protocol stem from its binary design and header compression mechanism, enabling attacks such as H2.CL and H2.TE desync exploits. These vulnerabilities allow for request smuggling, unauthorised access to sensitive information, and manipulation of content delivery on affected servers. Proper implementation and validation of request headers are crucial to mitigate these risks.
HTTP/2 vulnerabilities, particularly H2.TE and H2.X, allow for request header injection, request splitting, and desync attacks, leading to potential request smuggling and unauthorised access to sensitive data. Proper validation of headers and termination of headers during the downgrade process is essential to address these vulnerabilities.
Tunnelling exploitation in HTTP/2 enables attackers to bypass front-end security rules, leak internal headers, and perform cache poisoning, posing significant risks to website security. Robust security measures and thorough validation processes are necessary to mitigate these risks effectively.
Header Name Splitting, Request Line Injection, and Header Tampering Wrap are vulnerabilities in HTTP/2 that allow attackers to bypass security measures and manipulate server behaviour. Detection and exploitation of these vulnerabilities are challenging, requiring proper protocol implementation and validation practices.
Overall, HTTP/2's complexity has introduced new avenues for exploitation, highlighting the importance of robust security measures and awareness of potential risks in protocol implementation.


[Article used ](https://www.getambassador.io/blog/http3)

### What HTTP3 fixed  
HTTP/3 offers several advantages over HTTP/2, including improved resilience and reduced latency. These benefits are mainly attributed to the use of QUIC, which replaces TCP in TCP/IP. QUIC is built on top of UDP, which features a simpler connectionless communication model with minimal protocol mechanisms.
In HTTP/3, QUIC streams operate within the same connection but are delivered independently. This design provides greater flexibility in handling lossy or stalled connections compared to TCP. Additionally, HTTP/3 eliminates the head-of-line-blocking issue that persisted in HTTP/2, further enhancing performance and reliability.