gcloud functions deploy create_gym_playlist `
--gen2 `
--env-vars-file .env.yaml `
--runtime=python311 `
--region=europe-west1 `
--source=./src/serverless `
--entry-point=create_gym_playlist `
--trigger-http