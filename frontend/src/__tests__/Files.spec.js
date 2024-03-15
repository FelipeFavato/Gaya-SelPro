// npm i vitest start-server-and-test @vue/test-utils
// npm install -D @testing-library/vue
// Run the tests:
//  - npm run unit:test

import { describe, it, expect, vi, beforeEach } from 'vitest';
import Files from '../views/Files.vue';
import { mount } from '@vue/test-utils';

let mockGet = jest.fn();
jest.mock('axios', () => ({
  get: () => mockGet()
}));

describe('File', () => {

  beforeEach(() => {
    mockGet = jest.fn()
  })

  it('makes a GET request', async () => {
    const wrapper = factory();
    expect(mockGet).toHaveBeenCalledOnce();
  });

  it('should render correctly', () => {
    const wrapper = mount(Files);
    expect(wrapper.html()).toMatchSnapshot()
  });

  it('should render name input and change value', async () => {
    const wrapper = mount(Files);
    expect(wrapper.find('input[type="text"]').exists()).toBeTruthy();

    await wrapper.find('input[type="text"]').setValue('test');
    expect(wrapper.find('input[type="text"]').text('test'));
  });

  it('should render file input', () => {
    const wrapper = mount(Files);
    expect(wrapper.find('input[type="file"]').exists()).toBeTruthy();
  });

});