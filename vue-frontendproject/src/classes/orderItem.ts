import {Entity} from "@/interfaces/entity";

export class OrderItem implements Entity{
    id: number;
    product_title: string;
    quantity: number;
    price: number;

    constructor(id = 0, product_title = '', quantity = 0, price = 0) {
        this.id = id;
        this.product_title = product_title
        this.quantity = quantity;
        this.price = price;
    }
}