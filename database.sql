-- Create items table
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_offer BOOLEAN DEFAULT NULL
);

-- Insert some sample data
INSERT INTO items (name, price, is_offer) VALUES
    ('Laptop', 999.99, true),
    ('Mouse', 29.99, false),
    ('Keyboard', 59.99, true);

-- Create an index on the name field for faster searches
CREATE INDEX idx_items_name ON items(name); 