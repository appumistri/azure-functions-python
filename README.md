# Function App with Python SDKA lightweight serverless function app built with the Python SDK, demonstrating various trigger types such as Timer, HTTP, and Service Bus. This repository showcases how to hook up different Azure Functions triggers and integrate them into a cohesive application.

## Project Structure- `SampleTimerTrigger/` – Timer-triggered functions
- `SampleHttpTrigger/` – HTTP‑triggered functions
- `SampleServicebusTrigger/` – Service Bus‑triggered functions- `function_app.py` – Core application entry point
- `utils/` – Helper utilities and logging
- `infra/` – Infrastructure as Code (Terraform) for provisioning resources## Getting Started
1. **Install dependencies**  
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configurelocal.settings.json**  
   Add required environment variables (e.g., connection strings, app settings).

3. **Run locally**  
   ```bash   python function_app.py
   ```

4. **Deploy**  
   Use the Azure Functions Core Tools or ARM templates defined in `infra/` to deploy to Azure.

## Triggers Implemented
- **Timer Trigger** – Periodic background jobs (`SampleTimerTrigger`).
- **HTTP Trigger** – Expose REST endpoints (`SampleHttpTrigger`).
- **Service Bus Trigger** – React to messages from a Service Bus queue (`SampleServicebusTrigger`).

## License
MIT License – feel free to use and adapt for your own projects.

---  
*This README provides an overview; see individual module folders for detailed implementation notes.*