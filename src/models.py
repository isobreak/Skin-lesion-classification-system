import torch
import torchvision


def get_effnet(out: int = 1, freeze: bool = False) -> torch.nn.Module:
    """
    Perform some changes in architecture and returns model, arch (name)
    :param out: number of output neurons
    :param freeze: freeze conv layers
    :return: model
    """
    weights = torchvision.models.EfficientNet_B4_Weights.DEFAULT
    model = torchvision.models.efficientnet_b4(weights=weights)
    model.classifier = torch.nn.Sequential(
                torch.nn.Dropout(p=0.2, inplace=True),
                torch.nn.Linear(1792, out),
            )
    if freeze:
        for param in model.features.parameters():
            param.requires_grad = False
    return model


def get_inception(out: int = 1, freeze: bool = False) -> torch.nn.Module:
    """
    Perform some changes in architecture and returns model, arch (name)
    :param out: number of output neurons
    :param freeze: freeze conv layers
    :return: model
    """
    model = torchvision.models.inception_v3()
    if freeze:
        for param in model.parameters():
            param.requires_grad = False
    model.fc = torch.nn.Linear(2048, out)

    return model


def get_vgg(out: int = 1, freeze: bool = False) -> torch.nn.Module:
    """
    Perform some changes in architecture and returns model, arch (name)
    :param out: number of output neurons
    :param freeze: freeze conv layers
    :return: model
    """
    model = torchvision.models.vgg16(torchvision.models.VGG16_Weights.IMAGENET1K_V1)
    if freeze:
        for param in model.features.parameters():
            param.requires_grad = False
    model.classifier[6] = torch.nn.Linear(4096, out)

    return model


def get_resnet(out: int = 1, freeze: bool = False) -> torch.nn.Module:
    """
    Perform some changes in architecture and returns model, arch (name)
    :param out: number of output neurons
    :param freeze: freeze conv layers
    :return: model
    """
    model = torchvision.models.resnet50(weights='IMAGENET1K_V1')
    if freeze:
        for param in model.parameters():
            param.requires_grad = False
    model.fc = torch.nn.Linear(2048, out)

    return model


def get_densenet(out: int = 1, freeze: bool = False) -> torch.nn.Module:
    """
    Perform some changes in architecture and returns model, arch (name)
    :param out: number of output neurons
    :param freeze: freeze conv layers
    :return: model
    """
    model = torchvision.models.densenet121(weights='IMAGENET1K_V1')
    if freeze:
        for param in model.parameters():
            param.requires_grad = False
    model.classifier = torch.nn.Linear(1024, out)

    return model


if __name__ == "__main__":
    pass
