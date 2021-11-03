<template>
  <h2>Daily Sales</h2>

  <div id="chart"></div>
</template>

<script>
import {onMounted} from 'vue';
import axios from 'axios';
import * as c3 from 'c3';
export default {
  name: "Dashboard",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    onMounted(async () => {
      const chart = c3.generate({
        bindto: '#chart',

        data: {
          x: 'x',
          columns: [
            ['x'],
            ['Sales']
          ],
          types: {
            Sales: 'bar'
          },
        },
        axis: {
          x: {
            type: 'timeseries',
            tick: {
              format: '%Y-%m-%d'
            }
          }
        }
      });
      const response = await axios.get('orders/chart/');
      const records = response.data;
      chart.load({
        columns: [
          ['x', ...records.map(r => r.date)],
          ['Sales', ...records.map(r => r.total)]
        ]
      });
    });
  }
}
</script>