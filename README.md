# Github Terraform CDKTF

This repo contains the getting started code to use terraform CDKTF which uses the github provider.

## Getting Started

- Follow Getting Started Guide [here](https://learn.hashicorp.com/tutorials/terraform/cdktf)
- Have a look at cdktf getting started with python [here](https://learn.hashicorp.com/tutorials/terraform/cdktf-build-python?in=terraform/cdktf)

### Setting Up CDKTF

```shell
# Create an empty directory
mkdir github-terraform-cdktf

# Navigate to github-terraform-cdktf
cd github-terraform-cdktf

# Run cdktf init with python template and terraform backend as local to initialise cdktf directory with required modules installed and pipenv environment
cdktf init --template="python" --local
```

To install github provider include ```integrations/github@~> 4.14.0``` in cdktf.json>terraformProviders list. Run the following command to pull provider to imports folder.

```
cdktf get
```

### Authentication

To authenticate to github we need to create a personal token or app token with all required permissions and set GITHUB_TOKEN.

### Generating resource configuration

The following command creates resouce configurations in json format in cdktf.out.

```
cdktf synth
```

## Sync with existing resources(repository).

We can not get the configuration from existing resources using terraform import but we can generate terraform state file. So we will be generating the resource configuration and following command. We need to move to cdktf.out/stacks/github-terraform-cdktf and run following command. This will sync the existing resources to terraform state. Since we are using multi stack environment we need to provide the terraform state file as terraform.<stack_name>.tfstate

```
terraform import -state=../../../terraform.github-terraform-cdktf.tfstate github_repository.test_repo TestRepo
```

## Technical Stack

- Python
- Terraform
- Terraform CDKTF
- nodejs(Required to install cdktf)