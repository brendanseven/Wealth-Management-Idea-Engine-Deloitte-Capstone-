# AWS Deployment Guide

## Prerequisites

- AWS account with Bedrock access enabled
- EC2 key pair created in your target region
- Bedrock model access for Claude Haiku 4.5 (may require AWS Marketplace subscription)

## Option 1: CloudFormation Deployment

1. Go to **AWS Console > CloudFormation > Create stack**
2. Upload `cloudformation.yaml`
3. Fill in parameters:
   - **Stack name**: `idea-engine-stack`
   - **KeyPairName**: select your existing key pair
   - **InstanceType**: `t2.micro` (free tier) or `t2.small`
4. Acknowledge IAM resource creation and submit
5. Wait for `CREATE_COMPLETE` status (3-5 minutes)
6. Find the app URL in the **Outputs** tab

## Option 2: Manual Deployment

### 1. Launch EC2 Instance

- AMI: Ubuntu Server 24.04 LTS
- Instance type: `t2.micro` or `t2.small`
- Key pair: select or create one
- Security group: allow inbound TCP on ports 22, 80, 8501
- Attach IAM role with `AmazonBedrockFullAccess`

### 2. Connect and Install

```bash
ssh -i your-key.pem ubuntu@YOUR_PUBLIC_IP

sudo apt update && sudo apt install -y python3-pip python3-venv git
git clone https://github.com/brendanseven/Wealth-Management-Idea-Engine-Deloitte-Capstone-.git ~/idea-engine
cd ~/idea-engine
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

If the IAM role doesn't provide direct Bedrock access, configure credentials manually:

```bash
mkdir -p ~/.aws
nano ~/.aws/credentials
```

Add:
```
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
aws_session_token = YOUR_TOKEN   # if using temporary credentials
```

```bash
nano ~/.aws/config
```

Add:
```
[default]
region = us-east-2
```

### 4. Run the App

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Access at `http://YOUR_PUBLIC_IP:8501`.

### 5. (Optional) Auto-start on Boot

Create a systemd service:

```bash
sudo nano /etc/systemd/system/idea-engine.service
```

```
[Unit]
Description=Wealth Management Idea Engine
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/idea-engine
ExecStart=/home/ubuntu/idea-engine/venv/bin/streamlit run app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable idea-engine.service
sudo systemctl start idea-engine.service
```

## Stopping and Restarting

To save costs when not in use:

**Stop**: EC2 Console > select instance > Actions > Instance State > Stop
**Start**: Actions > Instance State > Start (note: public IP changes unless using an Elastic IP)

## Troubleshooting

**Expired token error**: AWS credentials have expired. Generate new access keys and update `~/.aws/credentials`.

**Bedrock access denied**: Ensure the IAM role has `AmazonBedrockFullAccess` and marketplace subscription policies. You may need to accept the Anthropic model terms through AWS Marketplace.

**Timeout errors**: The Bedrock client timeout is set to 120 seconds in `app.py`. If generation still times out, check your network or try a shorter prompt.

**Broken icon text in Streamlit**: The app includes a CSS fix for Streamlit's Material Symbols font loading issue. If icons appear as text, try `pip install --upgrade streamlit`.
