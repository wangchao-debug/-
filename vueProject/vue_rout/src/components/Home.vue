<template>
    <div>
        <h3>留言板界面</h3>
    <input type="text" v-model="msg">

    <button @click="add_note">添加留言</button>
    <ul v-for="(note,index) in msg_list" :key="index">
        <li>{{note}}<button @click="del_note(index)">删除</button></li>
    </ul>
        留言总数量：{{msg_list.length}}
    </div>
</template>

<script>
    export default {
        name: "Home",
        data(){
            return{
                msg:"",
            //判断localStorage是否有值，有值则显示，没有的话，设置成空数组
                msg_list:localStorage.msgs ?JSON.parse(localStorage.msgs):[]
            }
        },
        methods:{
                add_note(){
                    let msg = this.msg;
                    if(msg){
                        this.msg_list.push(this.msg);
                        localStorage.msgs = JSON.stringify(this.msg_list);

                        this.msg = "";
                    }
                },
                del_note(index){
                        this.msg_list.splice(index,1);
                        let res=JSON.parse(localStorage.msgs);
                        res.splice(index,1);
                        localStorage.msgs = JSON.stringify(res)
                },
        },
    }


</script>

<style scoped>

</style>
