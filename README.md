# Github Terraform CDKTF

This repo contains the getting started code to use terraform CDKTF which uses the github provider.

## Getting Started

- Follow Getting Started Guide [here](https://learn.hashicorp.com/tutorials/terraform/cdktf)
- Have a look at cdktf getting started with python [here](https://learn.hashicorp.com/tutorials/terraform/cdktf-build-python?in=terraform/cdktf)

## Sync with existing resources(repository).

We need to move to cdktf.out/stacks/github-terraform-cdktf and run following command. This will sync the existing resources to terraform state. Since we are using multi stack environment we need to provide the terraform state file as terraform.<stack_name>.tfstate

```
terraform import -state=../../../terraform.github-terraform-cdktf.tfstate github_repository.test_repo TestRepo
```

## Technical Stack

- Python
- Terraform
- Terraform CDKTF
- nodejs(Required to install cdktf)