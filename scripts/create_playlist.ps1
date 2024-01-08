Import-Module powershell-yaml
$yaml = gcloud functions describe create_gym_playlist | ConvertFrom-Yaml
$url = $yaml.url
$headers = @{
    'Authorization' = "bearer $(gcloud auth print-identity-token)"
}

Invoke-RestMethod -Uri $url -Method Get -Headers $headers