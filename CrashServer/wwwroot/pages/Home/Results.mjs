import { ref } from "vue"
import { useClient, useFormatters } from "@servicestack/vue"
 

export default {
  template:/*html*/`
    <auto-query-grid :header-titles="{Prediction:'Std Dev'}" type="ActiveGameResult" apis="QueryActiveRoomPredictionResults" :visible-from="{ name:'xl', bookingStartDate:'sm', bookingEndDate:'xl', createdBy:'2xl' }">
    </auto-query-grid>
 
  `,
  props: {  },
    setup() {
        
    }
}
