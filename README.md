# Analyzer for Computer Numerical Control Machines

Analyzer is used to detect errors on CNC machines, so users can quickly find the cause or error. In background, it creates failure tree analysis, so it can provide users with action plans or other solutions.

As of now, this is only a testing application, in the beta stage.

## Version, changes, updates

| Version | Supported          |  Comments                                                  |  Legal Requirements  |
| ------- | ------------------ |  --------------------------------------------------------- |  ------------------  |
| 0.8.5   | :white_check_mark: |  Database connections added                                                 |                      |
| 0.8.x   | :white_check_mark: |  Updated GUIs with KivyMD                                                |                      |
| 0.7.x   | :white_check_mark: |  Added fault tree table                                                 |                      |
| 0.6.x   | :white_check_mark: |  Updated structure, parameters added                                                |                      |
| 0.5.x   | :white_check_mark: |  Added desc, license, comms                                                 |                      |
| 0.4.x   | :white_check_mark: |                                                            |                      |
| 0.3.x   | :white_check_mark: |                                                            |                      |
| < 0.2   | :x:                |                                                            |                      |

## Communication protocols

There are several known CNC communication protocols that are commonly used in the CNC (Computer Numerical Control) industry. Some of the main CNC communication protocols are:

1. Modbus: Modbus is a widely used protocol for industrial communication. It allows communication between various devices over serial or Ethernet connections.

2. CAN (Controller Area Network): CAN is a robust and widely used protocol for communication in automotive and industrial applications.

3. RS-232 (Recommended Standard 232): RS-232 is a serial communication protocol commonly used for connecting CNC machines to computers or other devices.

4. RS-485 (Recommended Standard 485): RS-485 is another serial communication protocol that is used for longer-distance communication and can be used to connect multiple devices in a network.

5. TCP/IP (Transmission Control Protocol/Internet Protocol): TCP/IP is a suite of communication protocols used for communication over the internet and local networks. It is commonly used for connecting CNC machines to other computers or devices.

6. Profinet: Profinet is a real-time industrial Ethernet protocol used for communication in automation and control systems.

7. DeviceNet: DeviceNet is a communication protocol used for connecting industrial devices and sensors in a network.

8. Ethernet/IP: Ethernet/IP is an industrial Ethernet protocol that allows communication between various devices in automation and control systems.

9. EtherCAT: EtherCAT is a real-time Ethernet protocol that is used in motion control and automation applications.

10. Profibus: Profibus is a widely used fieldbus protocol for communication in automation and process control systems.

11. IO-Link: IO-Link is a communication protocol used for connecting sensors and actuators in industrial automation.


## FTA - Fault Tree Analysis

A general Fault Tree Analysis (FTA) table is a systematic way of representing potential failure modes and their contributing factors. It is commonly used to analyze complex systems and identify the root causes of failures. The table typically consists of several columns that describe the events, basic events, intermediate events, and the logical gates used to combine events. Here's a simplified version of a general FTA table:

| EVENT | DESCRIPTION         |  TYPE                                                 |  CAUSE  |
| ------- | ----------------------------------------------------------- |  ------------- |  ------------------  |
|Top Event| The main failure or undesired event | Top|                      |
|Basic Events    |Elementary failures or basic causes  | Leaf|Intermediate Events|
| Intermediate   |Combination of basic events or other intermediates  |Intermediate|Basic Events|
|AND Gate    |Logical AND gate combining multiple events  | Gate|Parent Events|
|OR Gate    |Logical OR gate combining multiple events  |Gate|Parent Events|
|NOT Gate    |Logical NOT gate for negating an event  |Gate|Single Events |


In this table, each row represents an event, which could be a top event (the main failure we want to analyze), a basic event (elementary failure or cause), or an intermediate event (a combination of basic events or other intermediate events).

The "Type" column specifies the type of event, which can be either "Top," "Leaf," or "Intermediate." The "Top" event is the main failure we are analyzing, "Leaf" events are basic events with no child events, and "Intermediate" events are combinations of other events.

The "Caused by" column indicates which events are combined using logical gates to form the current event. For example, an intermediate event may be the result of an AND gate combining multiple basic events, or it could be an OR gate combining different intermediate events.

Logical gates like AND, OR, and NOT are used to combine events in the FTA. These gates help trace the causal relationships between different events and determine the overall probability of the top event occurring.

Note that a real FTA table would be much more extensive, with many more events, logical gates, and descriptions. The goal is to systematically identify all possible failure modes and their causes to develop effective strategies for mitigating risks and improving system reliability.
