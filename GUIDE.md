# Guía de Instalación y Ejecución (eShopStore)

## Requisitos previos
- Python 3.10+
- Node.js + Angular CLI
- PostgreSQL
- Docker y Docker Compose
- Kubernetes (kubectl, minikube o cluster en la nube)
- Jenkins y Terraform instalados

## Pasos de instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/leoramzmusic/eShopStore.git
cd eShopStore
```

### 2. Configuración del Backend (Django)
1. Entrar al backend y crear entorno virtual:
   ```bash
   cd backend
   python -m venv venv
   ```
2. Activar entorno:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar base de datos PostgreSQL:
   ```sql
   CREATE DATABASE eshopstore;
   CREATE USER eshopuser WITH PASSWORD 'admin123.';
   GRANT ALL PRIVILEGES ON DATABASE eshopstore TO eshopuser;
   -- Important for PostgreSQL 15+
   \c eshopstore
   GRANT ALL ON SCHEMA public TO eshopuser;
   ```
5. Migrar modelos:
   ```bash
   python manage.py migrate
   ```
6. Crear superusuario:
   ```bash
   python manage.py createsuperuser
   ```
7. Ejecutar servidor:
   ```bash
   python manage.py runserver
   ```

### 3. Configuración del Frontend (Angular)
1. Instalar dependencias:
   ```bash
   cd frontend
   npm install --legacy-peer-deps
   ```
2. Ejecutar servidor frontend:
   ```bash
   ng serve
   ```

### 4. Ejecución con Docker
Para levantar todo el entorno de desarrollo local (incluyendo PostgreSQL y Redis):
1. Construir imágenes:
   ```bash
   docker-compose build
   ```
2. Levantar servicios:
   ```bash
   docker-compose up -d
   ```

### 5. Infraestructura y DevOps
- **Kubernetes:** Aplicar manifests de infraestructura base.
  ```bash
  kubectl apply -f devops/k8s/
  ```
- **Jenkins:** Configurar pipeline apuntando al `Jenkinsfile` en la raíz del proyecto.
- **Terraform:**
  ```bash
  cd devops/terraform
  terraform init
  terraform apply
  ```

## Notas Adicionales
- Configurar variables de entorno en archivos `.env` (backend y frontend) para credenciales y claves.
- En los entornos de producción, asegúrese de usar HTTPS con certificados SSL.
- Revise continuamente logs y métricas configurando **Prometheus y Grafana**.
