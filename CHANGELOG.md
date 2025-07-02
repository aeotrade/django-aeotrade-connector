# v0.1.0

**Release Date:** 📅 2024-12-23

## Overview

The **Django Aeotrade Connector** is a framework designed to simplify the creation of connectors for **Aeotrade OS**.
With this framework, you can easily integrate your connector with Aeotrade OS, enabling seamless communication and task
management.

## 🚀 New Features

- **✨ Autoload Tasks**
  Automatically loads tasks, including the heartbeat task, to ensure smooth task management and reduce manual
  intervention.

- **🔄 XML Parsing**
  Parses incoming XML messages from the message queue, ensuring seamless and efficient data handling.

- **⚙️ Custom Command for Initialization**
  Added two custom commands to initialize connector projects and automatically create connector applications,
  simplifying the setup process.

- **🐇 RabbitMQ Integration**
  Integrated **RabbitMQ** as the asynchronous message queue for better scalability and reliability in task processing.

- **📡 API Dispatcher**
  Common APIs are now wrapped in `dispatcher.py`, with automatic dispatching to the corresponding connectors,
  streamlining API communication.

- **⏳ Scheduler Enhancements**
  Custom scheduler tasks are now wrapped with distributed locking to ensure that only one task runs at a time,
  preventing task duplication.

- **📊 Task Status Reporting**
  Introduced functionality to report task status back to the **Aeotrade OS** server, providing better visibility into
  task progress.

- **🔌 MQ Manager**
  Added context management for message queues, with support for thread or process selection for listening during
  initialization, improving flexibility and performance.

- **📝 Task Models**
  Created django migrations file for connector task, execution logs, and message queue reception information,
  simplifying database management.

- **📦 Connector App Template**
  Introduced a new connector app template, simplifying the process of developing new connectors by providing a
  predefined structure.

- **🌐 Async/Sync HTTP Clients**
  Introduced both asynchronous and synchronous HTTP clients to offer flexibility in network communication, depending on
  use case requirements.

- **⚡ DRF Enhancements**
  Enhanced **Django Rest Framework (DRF)** request and response handling by adding serializer validation, exception
  handling, pagination, and other key components for better web development.

- **📦 Model Encoder**
  Enhanced encoder for converting Pydantic models to JSON, improving serialization efficiency and flexibility.
