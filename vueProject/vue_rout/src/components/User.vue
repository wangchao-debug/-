<template>
    <div>
        <table border="5">
        <tr>
            <td>ID</td>
            <td>姓名</td>
            <td>生日</td>
            <td>操作</td>
        </tr>
        <tr v-for="(user,index) in users" :key="user.id">
            <td>{{user.id}}</td>
            <td>{{user.name}}</td>
            <td>{{user.age}}</td>
            <td><a href="javascript:void(0)" @click="del_user(index)">删除</a>|<router-link :to="`/detail${user.id}`">查看用户详情</router-link></td>
        </tr>
        </table>
        <hr>
        用户名：<input type="text" v-model="name"> <br>
        生日：<input type="text" v-model="age"> <br>
        个人信息：<input type="text" v-model="id"> <br>
        <button @click="add_user">添加用户</button>
    </div>
</template>

<script>
    export default {
        name: "User",
        data(){
            return{
                 users:[
                     {"id":1,name:"武崇刚",age:"1900-02-31"},
                     {"id":2,name:"王超",age:"1999-06-15"},
                     {"id":3,name:"靳子昂",age:"1999-06-15"},
                     {"id":4,name:"林强",age:"1999-06-15"},
                     {"id":5,name:"康钦斌",age:"1999-06-15"},
                     ],
                name:"",
                id:"",
                age:"",
                msgs:{},
            }
        },
        methods:{
            add_user(){
                this.msgs["id"] = this.id;
                this.msgs["name"] = this.name;
                this.msgs["age"] = this.age;
                this.users.push(this.msgs)
            },
            del_user(index){
                // alert()
                this.users.splice(index,1);

            }
        }
    }


</script>

<style scoped>

</style>
