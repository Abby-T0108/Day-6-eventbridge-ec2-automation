# Day-6-eventbridge-ec2-automation
An automated system using AWS Lambda and EventBridge to stop EC2 instances that aren’t T2 micro type for cost control and governance

EventBridge EC2 Automation for Abbys World

Project Overview
This project demonstrates an automated system using AWS Lambda and EventBridge to monitor EC2 instances and automatically stop any instance that isn't a T2 micro type to control costs and enforce governance rules.

Steps:
1. Create Lambda Function: Automates the stopping of non-T2 micro EC2 instances.
2. Configure Lambda Permissions: Attach EC2 Full Access policy to the Lambda execution role.
3. Create EventBridge Rule: Triggers the Lambda function when an EC2 instance enters a "running" state.
4. Test the System: Launch T2 micro and non-T2 micro instances to see the automation in action.

How It Works:
- EventBridge watches for EC2 state changes.
- When an EC2 instance enters the "running" state, it triggers the Lambda function.
- Lambda checks the instance type, and if it's not T2 micro, it stops the instance.

Cost Control:
This automation helps prevent unnecessary costs by stopping instances that aren't cost-effective.
