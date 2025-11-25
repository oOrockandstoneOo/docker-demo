# Stage 1: builder
FROM alpine:3.20 AS builder
RUN mkdir -p /build/site
COPY index.html /build/site/

# Stage 2: runtime Nginx
FROM nginx:alpine
COPY --from=builder /build/site/ /usr/share/nginx/html/
EXPOSE 80
