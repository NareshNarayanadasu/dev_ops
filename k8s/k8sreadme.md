Sure, here's a `README.md` file incorporating all the commands and explanations.

```markdown
# Kubernetes Deployment Guide

## Hello World REST API Deployment with Docker and Kubernetes

This guide covers the steps to deploy a simple REST API using Docker and Kubernetes. Additionally, it includes commands for managing the deployment, scaling, and monitoring with Google Kubernetes Engine (GKE).

### Prerequisites

- Docker
- Kubernetes CLI (kubectl)
- Google Cloud SDK (gcloud)

### Docker

Run the Hello World REST API Docker container:

```bash
docker run -p 8080:8080 in28min/hello-world-rest-api:0.0.1.RELEASE
```

### Kubernetes

#### Creating and Managing Deployments and Services

1. **Create a Deployment**:
    ```bash
    kubectl create deployment hello-world-rest-api --image=in28min/hello-world-rest-api:0.0.1.RELEASE
    ```

2. **Expose the Deployment as a Service**:
    ```bash
    kubectl expose deployment hello-world-rest-api --type=LoadBalancer --port=8080
    ```

3. **Scale the Deployment**:
    ```bash
    kubectl scale deployment hello-world-rest-api --replicas=3
    ```

4. **Delete a Specific Pod**:
    ```bash
    kubectl delete pod hello-world-rest-api-58ff5dd898-62l9d
    ```

5. **Set Up Autoscaling**:
    ```bash
    kubectl autoscale deployment hello-world-rest-api --max=10 --cpu-percent=70
    ```

6. **Edit the Deployment**:
    ```bash
    kubectl edit deployment hello-world-rest-api
    # Set minReadySeconds: 15 in the editor
    ```

7. **Update the Deployment with a New Image**:
    ```bash
    kubectl set image deployment hello-world-rest-api hello-world-rest-api=in28min/hello-world-rest-api:0.0.2.RELEASE
    ```

#### GCloud and Kubernetes Setup

1. **Get Cluster Credentials**:
    ```bash
    gcloud container clusters get-credentials in28minutes-cluster --zone us-central1-a --project solid-course-258105
    ```

2. **Create and Expose the Deployment**:
    ```bash
    kubectl create deployment hello-world-rest-api --image=in28min/hello-world-rest-api:0.0.1.RELEASE
    kubectl expose deployment hello-world-rest-api --type=LoadBalancer --port=8080
    ```

3. **Set a Dummy Image for Testing**:
    ```bash
    kubectl set image deployment hello-world-rest-api hello-world-rest-api=DUMMY_IMAGE:TEST
    ```

4. **Retrieve and Sort Events**:
    ```bash
    kubectl get events --sort-by=.metadata.creationTimestamp
    ```

5. **Update the Deployment with a New Image Version**:
    ```bash
    kubectl set image deployment hello-world-rest-api hello-world-rest-api=in28min/hello-world-rest-api:0.0.2.RELEASE
    ```

6. **Get Component Statuses and List All Pods**:
    ```bash
    kubectl get componentstatuses
    kubectl get pods --all-namespaces
    ```

#### General Kubernetes Operations

1. **Get Events, Pods, ReplicaSets, Deployments, and Services**:
    ```bash
    kubectl get events
    kubectl get pods
    kubectl get replicaset
    kubectl get deployment
    kubectl get service
    ```

2. **Get Pods with Wide Output**:
    ```bash
    kubectl get pods -o wide
    ```

3. **Explain Pods**:
    ```bash
    kubectl explain pods
    ```

4. **Describe a Specific Pod**:
    ```bash
    kubectl describe pod hello-world-rest-api-58ff5dd898-9trh2
    ```

5. **Scale Deployment and Retrieve Lists**:
    ```bash
    kubectl scale deployment hello-world-rest-api --replicas=3
    kubectl get pods
    kubectl get replicaset
    kubectl get events
    kubectl get events --sort-by=.metadata.creationTimestamp
    kubectl get rs
    kubectl get rs -o wide
    ```

6. **Set Image and Describe Pods**:
    ```bash
    kubectl set image deployment hello-world-rest-api hello-world-rest-api=DUMMY_IMAGE:TEST
    kubectl get rs -o wide
    kubectl get pods
    kubectl describe pod hello-world-rest-api-85995ddd5c-msjsm
    kubectl get events --sort-by=.metadata.creationTimestamp
    kubectl set image deployment hello-world-rest-api hello-world-rest-api=in28min/hello-world-rest-api:0.0.2.RELEASE
    kubectl get events --sort-by=.metadata.creationTimestamp
    kubectl get pods -o wide
    ```

7. **Delete Specific Pods**:
    ```bash
    kubectl delete pod hello-world-rest-api-67c79fd44f-n6c7l
    kubectl get pods -o wide
    kubectl delete pod hello-world-rest-api-67c79fd44f-8bhdt
    ```

8. **Get Component Statuses and Pods in All Namespaces**:
    ```bash
    kubectl get componentstatuses
    kubectl get pods --all-namespaces
    ```

#### GCloud Authentication and Cluster Credentials

1. **Login to Google Cloud and Get Cluster Credentials**:
    ```bash
    gcloud auth login
    kubectl version
    gcloud container clusters get-credentials in28minutes-cluster --zone us-central1-a --project solid-course-258105
    ```

#### Rollout Management

1. **Manage Rollout History**:
    ```bash
    kubectl rollout history deployment hello-world-rest-api
    ```

2. **Set a New Image and Record the Update**:
    ```bash
    kubectl set image deployment hello-world-rest-api hello-world-rest-api=in28min/hello-world-rest-api:0.0.3.RELEASE --record=true
    ```

3. **Undo to a Specific Revision**:
    ```bash
    kubectl rollout undo deployment hello-world-rest-api --to-revision=1
    ```

#### Logs and Resource Inspection

1. **Retrieve and Follow Logs for Specific Pods**:
    ```bash
    kubectl logs hello-world-rest-api-58ff5dd898-6ctr2
    kubectl logs -f hello-world-rest-api-58ff5dd898-6ctr2
    ```

#### YAML Configuration

1. **Retrieve and Save YAML Configuration**:
    ```bash
    kubectl get deployment hello-world-rest-api -o yaml
    kubectl get deployment hello-world-rest-api -o yaml > deployment.yaml
    kubectl get service hello-world-rest-api -o yaml > service.yaml
    ```

2. **Apply YAML Configuration**:
    ```bash
    kubectl apply -f deployment.yaml
    kubectl get all -o wide
    kubectl delete all -l app=hello-world-rest-api
    ```

#### Monitoring and Cluster Information

1. **Monitor Services and Show Differences in Configurations**:
    ```bash
    kubectl get svc --watch
    kubectl diff -f deployment.yaml
    ```

2. **Delete Deployment and List Resources**:
    ```bash
    kubectl delete deployment hello-world-rest-api
    kubectl get all -o wide
    kubectl delete replicaset.apps/hello-world-rest-api-797dd4b5dc
    kubectl get pods --all-namespaces
    kubectl get pods --all-namespaces -l app=hello-world-rest-api
    kubectl get services --all-namespaces
    kubectl get services --all-namespaces --sort-by=.spec.type
    kubectl get services --all-namespaces --sort-by=.metadata.name
    kubectl cluster-info
    kubectl cluster-info dump
    kubectl top node
    kubectl top pod
    ```

#### Aliases and Shortcuts

1. **Shortened Commands to Get Resources**:
    ```bash
    kubectl get svc
    kubectl get ev
    kubectl get rs
    kubectl get ns
    kubectl get nodes
    kubectl get no
    kubectl get pods
    kubectl get po
    ```

#### Cleanup

1. **Delete Resources by Label and List All Resources**:
    ```bash
    kubectl delete all -l app=hello-world-rest-api
    kubectl get all
    ```

#### Applying Configurations

1. **Apply the Specified YAML Configurations**:
    ```bash
    kubectl apply -f deployment.yaml 
    kubectl apply -f ../currency-conversion/deployment.yaml 
    ```

## Conclusion

This guide provides a comprehensive set of commands to deploy and manage a simple REST API using Docker and Kubernetes on GKE. Adjust and expand these commands as needed for your specific use case.
```

Save this content into a file named `README.md`. This file will guide you through the steps to deploy a simple REST API and manage Kubernetes deployments on GKE. Adjust the commands and explanations as needed based on your specific project requirements.