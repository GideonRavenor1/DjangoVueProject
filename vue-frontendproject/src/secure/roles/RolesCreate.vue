<template>
  <form class="w-75 mt-3">
   <div class="form-group row">
      <label for="name" class="col-sm-2 col-form-label">Name</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" name="name" id="name" v-model="nameRole"/>
      </div>
    </div>
    <div class="form-group row">
      <label class="col-sm-2 col-form-label">Permissions</label>
      <div class="col-sm-10">
        <div class="form-check form-check-inline col-3" v-for="permission in permissions" :key="permission.id">
          <input class="form-check-input" type="checkbox" :value="permission.id"
                 @change="select(permission.id, $event.target.checked)"/>
          <label class="form-check-label">{{ permission.name }}</label>
        </div>
      </div>
    </div>
    <button class="btn btn-success" @click.prevent="submit">Create</button>
  </form>

</template>

<script>
import {ref, onMounted} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";


export default {
  name: "RolesCreate",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const nameRole = ref('');
    const permissions = ref([]);
    const selected = ref([]);
    const router = useRouter();

    onMounted(async () => {
      const response = await axios.get('users/permissions/');
      permissions.value = response.data.data;

        }
    );

    const select = (id, checked) => {
      if(checked){
        selected.value = [...selected.value, id];
        return;
      }
      selected.value = selected.value.filter(perm => perm !== id);
    }

    const submit = async () => {
       await axios.post('users/roles/', {
         name: nameRole.value,
         permissions: selected.value
      });
       await router.push('/roles');
    }

    return {
      nameRole,
      permissions,
      select,
      submit
    }
  }
}
</script>
