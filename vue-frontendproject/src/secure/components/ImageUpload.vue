<template>
  <label class="btn btn-primary">
    Upload<input type="file" hidden @change="upload($event.target.files)"/>
  </label>
</template>

<script lang="ts">
import axios from "axios";

interface ImageResponse {
  url: string
}
export default {
  name: "ImageUpload",
  emits: ['file-uploaded'],

  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup(props: any, context: any) {
     const upload = async(files: FileList) => {
      const file: File | null = files.item(0);
      const data = new FormData;
      if(file == null) return;
      data.append('image', file);
      const response = await axios.post<ImageResponse>('/products/upload/', data);

      context.emit('file-uploaded', response.data.url);
    };
     return {
       upload
     }

  }
}
</script>
