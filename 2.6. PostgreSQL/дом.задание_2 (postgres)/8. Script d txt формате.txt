CREATE TABLE homework_2.users (
   id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
   username VARCHAR(50) UNIQUE,
   email VARCHAR(100) UNIQUE,
   password VARCHAR(100),
   created_at DATE
);

CREATE TABLE homework_2.products (
   id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
   name VARCHAR(50),
   description VARCHAR(200),
   price NUMERIC,
   stock_quantity INTEGER,
   created_at DATE
);

CREATE TABLE homework_2.orders (
   id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
   user_id INTEGER,
   total_amount NUMERIC,
   order_date DATE,
   status text
   CHECK (status IN ('pending', 'completed', 'canceled')),
   FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE homework_2.reviews (
   id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
   product_id INTEGER,   
   user_id INTEGER,
   rating INTEGER
   CHECK (rating IN (1, 2, 3, 4, 5)),
   comment TEXT,
   created_at DATE,   
   FOREIGN KEY (user_id) REFERENCES users (id),
   FOREIGN KEY (product_id) REFERENCES products (id)   
);

CREATE TABLE homework_2.categories (
   id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
   name VARCHAR(50),
   description TEXT
);

ALTER TABLE homework_2.products ADD COLUMN category_id INTEGER, 
ADD FOREIGN KEY (category_id) REFERENCES categories(id);











