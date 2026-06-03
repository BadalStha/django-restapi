---

# 🛒 Project 2: E-Commerce Product Catalog REST API

A highly structured, stateless RESTful Web Service built using the Django REST Framework (DRF). This service acts as an independent backend engine exposing system data as structured JSON objects for modern frontend consumers.

## 🚀 API Architectural Features
- **Data Serialization Layer:** Implemented custom ModelSerializers to handle high-fidelity Python-to-JSON type casting.
- **RESTful Architecture:** Created explicit decoupled routing engines supporting structural GET, POST, and DELETE transaction protocols.
- **Token-Based Authentication Architecture:** Implemented a secure stateless request-validation architecture. Standard endpoints are locked globally, requiring valid cryptographic tokens passed via structural transport request headers (`Authorization: Token <hash>`).
- **Database Scaling:** Fully integrated tracking schemas into the enterprise PostgreSQL layer.

## 🛣️ API Endpoint Matrix

| Method | Endpoint | Access Control | Objective |
| :--- | :--- | :--- | :--- |
| **GET** | `/shop/api/products/` | Public | Fetches entire active product catalogs. |
| **POST** | `/shop/api/products/` | Public | Submits raw JSON data payload to append new inventory items. |
| **GET** | `/shop/api/products/<id>/` | **Token Required** | Evaluates a single specific item record matrix. |
| **DELETE** | `/shop/api/products/<id>/` | **Token Required** | Drops a target product entity directly out of relational storage. |
| **POST** | `/shop/api/api-token-auth/` | Public | Exchanges valid username/password payloads for session authentication tokens. |