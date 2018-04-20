# Deploying the app on kubernetes (minikube)
### Assumptions
1. It is assumed you have minikube installed.
2. The kubernetes version on minikube is 1.8.x.

## Steps

1. Set your kubectl context
```
kubectl config use-context minikube
```
2. Create the namespace for the app.

```
kubectl apply -f namespace.yml
```
3. Create the deployment 
```
kubectl apply -f deployment-app.yml
```
4. Create the service
```
kubectl apply -f Service.yml
```
5. Expose the service on minikube
```
minikube service leave-app-service -n tan-app
```
6. Check the service and port mapping
```
kubectl get svc -n tan-app
```
You should see something like this
```
NAME                   CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
leave-nginx-service   10.0.0.105   <nodes>       1234:31825/TCP   46m
```
Note the port mapping e.g 1234:31825, you will need it

7. Get the IP address of your minikube
```
minikube ip
```
copy this IP address

8. From step 7 and 8, we now have the ip address and nodeport with which we can visit our app e.g
```
http://192.168.99.100:31825/leave/login/
```
