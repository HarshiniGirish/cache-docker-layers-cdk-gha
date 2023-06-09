import os

from aws_cdk import aws_lambda
from aws_cdk.core import App, Stack 

class LambdaStack(Stack):
    def __init__(self, app, construct_id, **kwargs) -> None:
        super().__init__(app, construct_id, **kwargs)
        self.construct_id = construct_id
        
        code = (
            # create lambda with assets found in specified directory
            aws_lambda.Code.from_asset(ASSET_DIR)
            if (ASSET_DIR := os.getenv("BUILT_ASSET"))
            # create the lambda with code from a Dockerfile in ./lambda/Dockerfile
            else aws_lambda.Code.from_docker_build(
                path="./lambda", platform="linux/amd64"
            )
        )
                
        lambda_function = aws_lambda.Function(self, "function",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=code
        )

app = App()
test_stack = LambdaStack(app, "LambdaStack")
app.synth()