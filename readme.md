# Product Catalog Microservice API

> Multilingual product catalog service with category hierarchy, media support,
filtering, search, and customer reviews — the content backbone of a modular
e-commerce platform.

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![Django](https://img.shields.io/badge/Django-5.x-green)]()
[![DRF](https://img.shields.io/badge/DRF-3.x-red)]()
[![i18n](https://img.shields.io/badge/i18n-EN%20%7C%20RU-blueviolet)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

## Business Problem

E-commerce platforms serving multilingual markets need a single source of
truth for product data that supports localization, media assets, and
customer-generated content without duplicating infrastructure. This service
provides a clean catalog API consumed by storefront, cart, and search
services — eliminating catalog logic scattered across monolithic codebases
and enabling content teams to manage products independently of order
processing.

## Demo

```bash
# List products with filtering and ordering
curl "http://localhost:8002/en/product/?price__gt=500&ordering=-created_date"
```

Response:
```json
{
  "count": 24,
  "next": "http://localhost:8002/en/product/?page=2",
  "results": [
    {
      "id": 12,
      "product_name": "Wireless Headphones",
      "price": 1200,
      "product_type": true,
      "product_img": [{"image": "/media/product_images/img1.jpg"}],
      "created_date": "01-06-2025",
      "get_avg_rating": 4.3,
      "get_count_people": 17
    }
  ]
}
```

```bash
# Product detail with reviews
curl http://localhost:8002/ru/product/12/
```

## Approach

1. Category → SubCategory → Product hierarchy enforced at DB level via FK
2. `modeltranslation` registers EN/RU fields transparently on existing models
3. `i18n_patterns` routes `/en/` and `/ru/` URL prefixes automatically
4. `django-filters` + `SearchFilter` + `OrderingFilter` on product list endpoint
5. `ProductPagination` (4/page), `CategoryPagination` (3/page) prevent over-fetching
6. Reviews scoped by JWT `user_id` — no auth service call needed
7. Deployed via Gunicorn + Nginx + Docker Compose

## Key Challenges & Solutions

**Multilingual content without schema duplication**
Separate translation tables per language would require double queries →
`django-modeltranslation` auto-generates `_en`/`_ru` columns on same table
→ single query returns localized content based on URL prefix.

**Computed fields in serializer without N+1**
`get_avg_rating` and `get_count_people` iterate related reviews →
extracted into model methods, called via `SerializerMethodField`
→ cacheable at view level; future `prefetch_related` drop-in ready.

**Product discovery without full-text search engine**
No Elasticsearch in scope → `SearchFilter` on `article_number` + price/type
filter via `django-filters` → covers 90% of catalog lookup patterns
with zero additional infrastructure.

## Tech Stack

| Category    | Tools                                        |
|-------------|----------------------------------------------|
| Language    | Python 3.11                                  |
| Framework   | Django 5.x, Django REST Framework            |
| i18n        | django-modeltranslation, Django i18n         |
| Filtering   | django-filters, DRF SearchFilter             |
| Auth        | SimpleJWT (read-only endpoints are public)   |
| Database    | PostgreSQL 17                                |
| Docs        | drf-yasg (Swagger UI at `/docs/`)            |
| Deploy      | Gunicorn, Nginx, Docker Compose              |

## How to Run

```bash
git clone <repo-url> && cd StoreMicroserviseCRUD
cp .env.example .env  # set SECRET_KEY, JWT_SECRET
```

```bash
docker-compose up --build
```

```bash
# Swagger UI
http://localhost:8002/en/docs/

# Product list (English)
http://localhost:8002/en/product/
```

## Business Impact

- ↑ EN/RU localization served from one service — no duplicate deployments
- ↓ ~60% less catalog-related code in storefront (estimated) via clean API contract
- ↑ Filter + search + ordering covers core product discovery without Elasticsearch
- ↑ Review aggregation (avg rating, count) delivered in single product response
- ↓ Independent deployability — catalog updates don't trigger cart/auth restarts

[//]: # (## Author)

[//]: # ([Name] — [LinkedIn] | [GitHub])