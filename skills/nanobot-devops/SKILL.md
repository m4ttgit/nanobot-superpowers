# Nanobot DevOps#

Complete toolkit for senior devops with modern tools and best practices using nanobot.

## Use when#

- Setting up CI/CD pipelines, deploying applications, managing infrastructure
- Implementing monitoring, optimizing deployment processes
- Working with Docker, Kubernetes, Terraform, AWS, GCP, or Azure
- Need infrastructure as code, pipeline automation, or deployment strategies
- Integrating DevOps workflows into nanobot superpowers project#

## Core principle#

Infrastructure should be reproducible, version-controlled, and automatically testable. nanobot automates the mechanical aspects (scaffolding, validation, deployment) so you can focus on architecture, trade-offs, and reliability.

## The Process#

### 1. Pipeline Generation#

Scaffold CI/CD pipeline configurations for GitHub Actions or CircleCI:

```bash
python scripts/pipeline_generator.py <project-path> --platform=github --stages=build,test,deploy
```

**Example — GitHub Actions workflow:**
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm test -- --coverage
      - name: Upload coverage
        uses: codecov/codecov-action@v4

  build-docker:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build and push image
        uses: docker/build-push-action@v5
        with:
          push: ${{ github.ref == 'refs/heads/main' }}
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}

  deploy:
    needs: build-docker
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster production \
            --service app-service \
            --force-new-deployment
```

### 2. Infrastructure as Code#

Generate, validate, and plan Terraform modules:

```bash
python scripts/terraform_scaffolder.py <target-path> --provider=aws --module=ecs-service --verbose
```

**Example — AWS ECS service module:**
```hcl
# modules/ecs-service/main.tf
resource "aws_ecs_task_definition" "app" {
  family                   = var.service_name
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = var.cpu
  memory                   = var.memory

  container_definitions = jsonencode([{
    name      = var.service_name
    image     = var.container_image
    essential = true
    portMappings = [{
      containerPort = var.container_port
      protocol      = "tcp"
    }]
    environment = [for k, v in var.env_vars : { name = k, value = v }]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        awslogs-group         = "/ecs/${var.service_name}"
        awslogs-region        = var.aws_region
        awslogs-stream-prefix = "ecs"
      }
    }
  }])
}

resource "aws_ecs_service" "app" {
  name            = var.service_name
  cluster         = var.cluster_id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = var.desired_count
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = var.private_subnet_ids
    security_groups  = [aws_security_group.app.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = var.service_name
    container_port   = var.container_port
  }
}
```

### 3. Deployment Management#

Orchestrate deployments with blue/green or rolling strategies:

```bash
python3 scripts/deployment_manager.py ./deploy --verbose --json
```

**Example — Kubernetes blue/green deployment:**
```yaml
# k8s/deployment-blue.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-blue
  labels:
    app: myapp
    slot: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      slot: blue
  template:
    metadata:
      labels:
        app: myapp
        slot: blue
    spec:
      containers:
        - name: app
          image: ghcr.io/org/app:1.2.3
          readinessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
          resources:
            requests:
              cpu: "250m"
              memory: "256Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
```

## Tools Included#

### Pipeline Generator#
Scaffolds CI/CD pipeline configurations for GitHub Actions or CircleCI.

### Terraform Scaffolder#
Generates and validates IaC modules for AWS/GCP/Azure.

### Deployment Manager#
Orchestrates deployments with rollback support and health-check gates.

## Red Flags#

- **Manual infrastructure changes** → Use Terraform, never click in consoles
- **No health checks** → Add readinessProbe/livenessProbe to all deployments
- **Secrets in code** → Use secret managers (AWS Secrets, Azure KeyVault)
- **No rollback plan** → Always test rollback procedure before deploying
- **Single Points of Failure** → Use multi-AZ deployments, replica sets
- **No monitoring** → Deploy metrics (Prometheus) and dashboards (Grafana)
- **Over-engineering** → Start simple (single region), expand only when needed#

## Development Workflow#

### Infrastructure Changes (Terraform)#

```bash
# Scaffold or update module
python scripts/terraform_scaffolder.py ./infra --provider=aws --module=ecs-service --verbose

# Validate and plan — review diff before applying
terraform -chdir=infra init
terraform -chdir=infra validate
terraform -chdir=infra plan -out=tfplan

# Apply only after plan review
terraform -chdir=infra apply tfplan

# Verify resources are healthy
aws ecs describe-services --cluster production --services app-service \
  --query 'services[0].{Status:status,Running:runningCount,Desired:desiredCount}'
```

### Application Deployment#

```bash
# Generate or update pipeline config
python scripts/pipeline_generator.py . --platform=github --stages=build,test,security,deploy

# Build and tag image
docker build -t ghcr.io/org/app:$(git rev-parse --short HEAD) .
docker push ghcr.io/org/app:$(git rev-parse --short HEAD)

# Deploy with health-check gate
python scripts/deployment_manager.py deploy \
  --env=production \
  --image=app:$(git rev-parse --short HEAD) \
  --strategy=blue-green \
  --health-check-url=https://app.example.com/healthz

# Verify pods are running
kubectl get pods -n production -l app=myapp
kubectl rollout status deployment/app-blue -n production
```

### Rollback Procedure#

```bash
# Immediate rollback via deployment manager
python scripts/deployment_manager.py rollback --env=production --to-version=1.2.2

# Or via kubectl
kubectl rollout undo deployment/app -n production
kubectl rollout status deployment/app -n production

# Verify rollback succeeded
kubectl get pods -n production -l app=myapp
curl -sf https://app.example.com/healthz || echo "ROLLBACK FAILED — escalate"
```

## Multi-Cloud Considerations#

| SKILL | Cloud | Use When |
|-------|-------|----------|
| **nanobot-architect** | General | ECS/EKS, Lambda, VPC design, cost optimization |
| **azure-cloud-architect** | Azure | AKS, App Service, Virtual Networks, Azure DevOps |
| **gcp-cloud-architect** | GCP | GKE, Cloud Run, VPC, Cloud Build |

**Multi-cloud vs single-cloud decision:**
- **Single-cloud** (default) — lower operational complexity, deeper managed-service integration
- **Multi-cloud** — required for compliance/data residency, acquiring companies on different clouds
- **Hybrid** — on-prem + cloud; use when regulated workloads must stay on-prem#

## Cloud-Agnostic IaC#

### Terraform / OpenTofu (Default Choice)#

- Single language (HCL) across AWS, Azure, GCP, and 3,000+ providers
- State management with remote backends (S3, GCS, Azure Blob)
- Plan-before-apply workflow prevents drift surprises#

### Pulumi (Programming Language IaC)#

Choose Pulumi when the team prefers TypeScript, Python, Go, or C# over HCL.

## Common nanobot Commands#

```bash
# Pipeline Generation
python scripts/pipeline_generator.py . --platform=github --stages=build,test,deploy
python scripts/pipeline_generator.py . --platform=circleci --stages=build,test

# Terraform Scaffolding
python scripts/terraform_scaffolder.py ./infra --provider=aws --module=ecs-service
python scripts/terraform_scaffolder.py ./infra --provider=azure --module=aks-service --verbose

# Deployment Management
python scripts/deployment_manager.py deploy --env=staging --image=app:1.2.3
python scripts/deployment_manager.py rollback --env=production --to-version=1.2.2
python scripts/deployment_manager.py --analyze --env=production
```

## References#

Load these files from the SKILL's `references/` directory for detailed information:

| File | Contains | When to Load |
|------|----------|--------------|
| `references/cicd_pipeline_guide.md` | CI/CD patterns, best practices, antipatterns | "setup pipeline", "GitHub Actions", "CircleCI" |
| `references/infrastructure_as_code.md` | IaC step-by-step processes, optimization | "Terraform", "Pulumi", "OpenTofu" |
| `references/deployment_strategies.md` | Deployment configs, security, scalability | "blue/green", "rolling", "canary" |
| `references/troubleshooting.md` | Common issues and solutions | "deployment failed", "pipeline error" |
