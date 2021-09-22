#!/usr/bin/env python

# Construct class holds building blocks of a system. Please refer below URL 
#  https://docs.aws.amazon.com/cdk/latest/guide/constructs.html
from constructs import Construct
from cdktf import App, TerraformStack
from imports.github import GithubProvider, Repository

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # Replace the owner below with your github username
        GithubProvider(self, "Github", owner="vishnu-chegondi") 

        Repository(
            self,
            "test_repo",
            name="TestRepo",
            description="This is test repo created as a part of getting started guide for terraform cdktf",
            visibility="public"
            )

# Every class App, MyStack, Repositories are of type Constructs
# App is the root node of constructs.
app = App()
MyStack(app, "github-terraform-cdktf")

app.synth()
