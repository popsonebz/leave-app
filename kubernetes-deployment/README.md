# Deploying the app on kubernetes (minikube)
### Assumptions
1. It is assumed you have minikube installed.
2. The kubernetes version on minikube is 1.8.x.

## Steps

1. Set your kubectl context
```
kubectl config use-context minikube
```
2. Use your terminal to navigate into app-deployment directory

3. Apply the namespace for the app.

```
kubectl apply -f namespace.yml
```
4. apply the deployment 
```
kubectl apply -f deployment-app.yml
```
5. Check if the pod is up and running (it takes approximately 2 minutes)
```
kubectl get pods -n tan-app
```
6. Apply the service
```
kubectl apply -f Service.yml
```
7. Create the network policy
```
kubectl apply -f networkpolicy.yml
```
8. Navigate into nginx-deployment directory

9. Apply the nginx deployment
```
kubectl apply -f deployment-nginx.yml
```

10. Expose the deployment so you can access it from your browser
```
kubectl expose deployment leave-nginx-deployment -n tan-app --type=NodePort
kubectl expose deployment leave-app-deployment -n tan-app --type=NodePort
```
11. Expose the service on minikube
```
minikube service leave-app-service -n tan-app
```
12. Check the service and port mapping
```
kubectl get svc -n tan-app
```
You should see something like this
```
NAME                   CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
leave-app-deployment   10.0.0.105   <nodes>       1234:31825/TCP   46m
leave-nginx-deployment   10.0.0.105   <nodes>       1234:31825/TCP   46m
```
Note the port mapping e.g 1234:31825, you will need it

13. Get the IP address of your minikube
```
minikube ip
```
copy this IP address

14. Navigate back into app-deployment directory

15. Enable ingress on the cluster

```
minikube addons enable ingress
```
16. Create an ingress resource
```
kubectl apply -f ingress.yml
```
17. Edit your hosts file to add the ip address of minikube and leave.com at the last line of the file e.g
```
192.168.99.100 leave.com
```
18. Open your *Chrome* browser and visit this url to register an employee
```
leave.com/admin/add-employee
```
19. The employee can now login using the url below and the details from the above step
```
leave.com/leave/apply
```
