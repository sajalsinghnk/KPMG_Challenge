# To Create a VPC

resource "aws_vpc" "myvpc"{
    cidr_block = "10.0.0.0/16"
}


# To Create public subnets in 2 availability zone

resource "aws_subnet" "PublicSubnetA"{
    vpc_id = aws_vpc.myvpc.id
    cidr_block = "10.0.0.0/28"
    availability_zone = "us-east-1a"
}

resource "aws_subnet" "PublicSubnetB"{
    vpc_id = aws_vpc.myvpc.id
    cidr_block = "10.0.0.16/28"
    availability_zone = "us-east-1b"
}


# To create private subnets in 2 availability zone

resource "aws_subnet" "PrivSubnetA"{
    vpc_id = aws_vpc.myvpc.id
    cidr_block = "10.0.0.32/28"
    availability_zone = "us-east-1a"
}

resource "aws_subnet" "PrivSubnetB"{
    vpc_id = aws_vpc.myvpc.id
    cidr_block = "10.0.0.48/28"
    availability_zone = "us-east-1b"
}


# To create Internet Gateway

resource "aws_internet_gateway" "myIgw"{
    vpc_id = aws_vpc.myvpc.id
}


# To create route Tables for public subnet

resource "aws_route_table" "PublicRT"{
    vpc_id = aws_vpc.myvpc.id
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.myIgw.id
    }
}
 

# To create route table association with public subnets 

resource "aws_route_table_association" "PublicRTAssociationA"{
    subnet_id = aws_subnet.PublicSubnetA.id
    route_table_id = aws_route_table.PublicRT.id
}

resource "aws_route_table_association" "PublicRTAssociationB"{
    subnet_id = aws_subnet.PublicSubnetB.id
    route_table_id = aws_route_table.PublicRT.id
}
