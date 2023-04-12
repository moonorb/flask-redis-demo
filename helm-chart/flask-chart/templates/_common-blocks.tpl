{{- define "ContainerPortHERE"}}
ports:
  - containerPort: {{.Values.ContainerPortNumber}}
{{- end}}


{{/*
Indent here Does matter for the part inside the function. 
Indent for the first and last lines dont matter. 

 So this looks really ugly but it works.
        {{- define "ContainerPortHERE"}}
ports:
  - containerPort: {{.Values.ContainerPortNumber}}
         {{- end}}

*/}}