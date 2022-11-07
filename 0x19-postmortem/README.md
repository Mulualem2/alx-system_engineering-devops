# Ethio Telecom Server Error
## Issue Summary
From 10:30 PM to 8:30 AM, Ethio telecome server was  experienced an outage
due to a prescheduled reboot that ended in failure. The points of failure are coming from the rebooting of the load balancer or cache server. 
The Security Team issued a maintenance update and a reboot notification to a major server on May 10, 2020 for a window of 4 hours (10:30 to 2:30 AM). 
Security Team is patching a security vulnerability in the Program. 
Customers reaching the site after the reboot scheduled time of 2:30 AM to 8:30 AM could not reach the site, affecting 100% of them. 
The root cause of the outage was due to the data on the the server not auto-mounting at boot time. 
The SRE mistakenly acknowledged the incident as something normal during a server reboot and closed all subsequent alerts.
Timeline (all times in Pacific Time)
- 10:30 PM: Reboot begins
- 12:26 AM: Outage begins
- 12:26 AM: Alerts sent to teams
- 12:30 AM: Lead SRE silenced all subsequent alerts due to server behavior being “normal”
- 2:30 AM: Server down and customers can’t reach the site
- 2:30 AM: Alerts sent to teams
- 2:35 AM: A ticket was opened and a database service provider personnel sent over within 30 minutes.
- 3:15 AM: Personnel arrives to assess the situation
- 4:30 AM: Server restarts begin
- 8:30 AM: 100% of traffic back online
## Root Cause
At 12:26 AM, the reboot of the load-balancer or cache server continued to fail. The failover server (secondary server) did not come back up for for 3 hours. 
We did not expect the scheduled reboot to affect our systems. The software update was fine, yet it affected the overall performance of the site. 
It was not reconnecting to the secondary server. Personnel from the database service provider investigated that the data on the server did not auto-mount at boot time. 
Our lead SRE claims the incident to be a routine behavior of a server reboot, thus any further alerts were silenced automatically.
## Resolution and Recovery
- At 2:35 AM, a ticket was opened to fix the down server and sent out to the database service provider personnel. The team arrived at 3:15 AM.
- The NSX CLI is used to get detailed information about tail logs and take packet captures. It also, looks at the metrics for trouble shooting the load balancer.
- Verification of basic services are running by checking the routing table.
- The auto-mount was not successful and a new mount was manually placed by the database service provider personnel at 4:30 AM.
- Processes started to recover slowly. We estimated time to reboot and recovery time to span 4 hours.
- To help with recovery, we retarted affected servers. SRE engineers, manually restarted unicorn processes on the web application servers to further correct the reboot process.
- The process was slow to prevent any possible cascading failures and to avoid a wide scale reboot — affecting our customers even further.
- By 8:30 AM, traffic was restored and 100% of our customers reported back with no issues.
## Corrective and Preventative Measures
- In the last 3 days, we’ve made an internal review and analysis of the outage. The following measures are actions the team will follow for prevention and to improve response times in the future.
- The database server provider during the performance degradation could have alerted teams by noting that the down server was not routine behavior. An update to their systems to prevent further issues in the future are done accordingly.
- The Security Team did not properly plan the reboot schedule affecting many of our customers. There was no available staff to monitor the reboot and to access the situation right away in a timely manner.
- There were no engineers present to possibly resolve the situation by manually fixing any issues that came up.
- For scheduled reboots like this, there should be a 24 hour operations rotation in order to monitor every aspect of the update.
