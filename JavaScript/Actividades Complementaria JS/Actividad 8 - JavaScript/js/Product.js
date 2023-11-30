/**
 * Product Class
 */
export class Product {
  /**
   *
   * @param {string} name 
   * @param {number} cantThe Product Name
   * @param {number} price The Product Price
   * @param {number} year The year creation of the Product
   * 
   */
  constructor(name, cant, price, year) {
    this.name = name;
    this.cant = cant;
    this.price = price;
    this.year = year;
  }
}
