from dataclasses import dataclass


@dataclass
class CheckType:
    BITBUCKET_PIPELINES = "bitbucket_pipelines"
    CIRCLECI_PIPELINES = "circleci_pipelines"
    ARGO_WORKFLOWS = "argo_workflows"
    ARM = "arm"
    BICEP = "bicep"
    CLOUDFORMATION = "cloudformation"
    DOCKERFILE = "dockerfile"
    GITHUB_CONFIGURATION = "github_configuration"
    GITHUB_ACTIONS = "github_actions"
    GITLAB_CONFIGURATION = "gitlab_configuration"
    GITLAB_CI = "gitlab_ci"
    BITBUCKET_CONFIGURATION = "bitbucket_configuration"
    HELM = "helm"
    JSON = "json"
    YAML = "yaml"
    KUBERNETES = "kubernetes"
    KUSTOMIZE = "kustomize"
    OPENAPI = "openapi"
    SCA_PACKAGE = "sca_package"
    SCA_IMAGE = "sca_image"
    SECRETS = "secrets"
    SERVERLESS = "serverless"
    TERRAFORM = "terraform"
    TERRAFORM_PLAN = "terraform_plan"