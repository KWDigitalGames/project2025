variable "db_username" {
  type = string
}

variable "password" {
  type = string
}


provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "project2025" {
  name     = "project2025"
  location = "Australia East"
}

resource "azurerm_virtual_network" "rpgappnetwork" {
  name                = "rpgapp-network"
  location            = "polandcentral"
  resource_group_name = "project2025"
  address_space       = ["10.0.0.0/16"]
}

resource "azurerm_subnet" "rpgapp-subnet" {
  name                 = "rpaapp-subnet"
  resource_group_name  = "project2025"
  virtual_network_name = "rpgapp-network"
  address_prefixes     = ["10.0.2.0/24"]
  service_endpoints    = ["Microsoft.Storage"]
  delegation {
    name = "fs"
    service_delegation {
      name = "Microsoft.DBforPostgreSQL/flexibleServers"
      actions = [
        "Microsoft.Network/virtualNetworks/subnets/join/action",
      ]
    }
  }
}

resource "azurerm_private_dns_zone" "dns" {
  name                = "rpgapp.postgres.database.azure.com"
  resource_group_name = "project2025"
}

resource "azurerm_private_dns_zone_virtual_network_link" "rpgapp-private-dns-zone" {
  name                  = "rpgapp-dns-zone"
  private_dns_zone_name = "rpgapp.postgres.database.azure.com"
  virtual_network_id    = azurerm_virtual_network.rpgappnetwork.id
  resource_group_name   = "project2025"
  depends_on            = [azurerm_subnet.rpgapp-subnet]
}

resource "azurerm_postgresql_flexible_server" "postgres" {
  name                          = "rpgapp-postgres"
  resource_group_name           = "project2025"
  location                      = "polandcentral"
  version                       = "13"
  delegated_subnet_id           = azurerm_subnet.rpgapp-subnet.id
  private_dns_zone_id           = azurerm_private_dns_zone.dns.id
  administrator_login           = var.db_username
  administrator_password        = var.password
  zone                          = "1"

  storage_mb   = 32768

  sku_name   = "B_Standard_B1ms"
  depends_on = [azurerm_private_dns_zone_virtual_network_link.rpgapp-private-dns-zone]

  }