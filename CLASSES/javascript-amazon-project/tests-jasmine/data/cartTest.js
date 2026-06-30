import {addToCart,cart,loadFromStorage} from '../../data/cart.js';
console.log('fooyou');

// didn't work well 0509-2025, interesting concept of testing framework
// not sure if it was TJ issue or [code drift] since course was written.
describe('test suite add to cart', () => {
  it('adds an existing product to the cart',() => {
    spyOn(localStorage,'setItem');
    spyOn(localStorage,'getItem').and.callFake(() => {
      return JSON.stringify([{
        prouctId: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
        quantity: 1,
        deliveryOptionId: '1'
      }]);
    });
    loadFromStorage();
    addToCart('e43638ce-6aa0-4b85-b27f-e1d07eb678c6');
    expect(cart.length).toEqual(1);
    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(cart[0].productId).toEqual('e43638ce-6aa0-4b85-b27f-e1d07eb678c6');
    expect(cart[0].quantity).toEqual(2);
  });

  it('adds a new product to the cart'), () => {
    spyOn(localStorage,'getItem').and.callFake(() => {
      return JSON.stringify([]);
    });
    loadFromStorage();
    console.log('foo');
    console.log(localStorage.getItem('cart'));
    addToCart('e43638ce-6aa0-4b85-b27f-e1d07eb678c6');
    expect(cart.length).toEqual(1);
    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(cart[0].prouctId.toEqual('e43638ce-6aa0-4b85-b27f-e1d07eb678c6'));
    expect(cart[0].quantity).toEqual(2);
  }
});