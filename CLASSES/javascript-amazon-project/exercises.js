<script>
import dayjs from 'https://unpkg.com/supersimpledev@8.5.0/dayjs/esm/index.js';
const today = dayjs();
      const deliveryDate = today.add(
        5, 
        'days'
      );

const dateString = deliveryDate.format('dddd, MMMM D');

console.log(dateString);
</script>

