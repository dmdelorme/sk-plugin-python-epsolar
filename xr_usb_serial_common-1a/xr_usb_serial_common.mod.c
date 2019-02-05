#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x367398b6, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x7f873ed8, __VMLINUX_SYMBOL_STR(usb_deregister) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0x375d776a, __VMLINUX_SYMBOL_STR(put_tty_driver) },
	{ 0x2ba8937e, __VMLINUX_SYMBOL_STR(tty_unregister_driver) },
	{ 0xebdc0b9a, __VMLINUX_SYMBOL_STR(usb_register_driver) },
	{ 0x43bef699, __VMLINUX_SYMBOL_STR(tty_register_driver) },
	{ 0xcbdf8d64, __VMLINUX_SYMBOL_STR(tty_set_operations) },
	{ 0x67b27ec1, __VMLINUX_SYMBOL_STR(tty_std_termios) },
	{ 0xaadaa117, __VMLINUX_SYMBOL_STR(__tty_alloc_driver) },
	{ 0x4e86098e, __VMLINUX_SYMBOL_STR(tty_port_register_device) },
	{ 0x7b03c48, __VMLINUX_SYMBOL_STR(usb_get_intf) },
	{ 0x5e4d70d3, __VMLINUX_SYMBOL_STR(usb_driver_claim_interface) },
	{ 0xb995cc87, __VMLINUX_SYMBOL_STR(_dev_info) },
	{ 0x12da5bb2, __VMLINUX_SYMBOL_STR(__kmalloc) },
	{ 0x7fafcb5a, __VMLINUX_SYMBOL_STR(device_create_file) },
	{ 0x795b774c, __VMLINUX_SYMBOL_STR(dev_warn) },
	{ 0x9174a2a3, __VMLINUX_SYMBOL_STR(usb_alloc_urb) },
	{ 0xcee6191d, __VMLINUX_SYMBOL_STR(usb_alloc_coherent) },
	{ 0xc1065dac, __VMLINUX_SYMBOL_STR(tty_port_init) },
	{ 0x2aee63f4, __VMLINUX_SYMBOL_STR(__mutex_init) },
	{ 0x33c4c33d, __VMLINUX_SYMBOL_STR(usb_ifnum_to_if) },
	{ 0xbc10dd97, __VMLINUX_SYMBOL_STR(__put_user_4) },
	{ 0x7a9f42fb, __VMLINUX_SYMBOL_STR(kmem_cache_alloc_trace) },
	{ 0x7f9f07e3, __VMLINUX_SYMBOL_STR(kmalloc_caches) },
	{ 0xf4fa543b, __VMLINUX_SYMBOL_STR(arm_copy_to_user) },
	{ 0xfa2a45e, __VMLINUX_SYMBOL_STR(__memzero) },
	{ 0x353e3fa5, __VMLINUX_SYMBOL_STR(__get_user_4) },
	{ 0xc6cbbc89, __VMLINUX_SYMBOL_STR(capable) },
	{ 0x28cc25db, __VMLINUX_SYMBOL_STR(arm_copy_from_user) },
	{ 0x71c90087, __VMLINUX_SYMBOL_STR(memcmp) },
	{ 0x409873e3, __VMLINUX_SYMBOL_STR(tty_termios_baud_rate) },
	{ 0xe707d823, __VMLINUX_SYMBOL_STR(__aeabi_uidiv) },
	{ 0xc7d32ef9, __VMLINUX_SYMBOL_STR(usb_autopm_put_interface) },
	{ 0x4e8123da, __VMLINUX_SYMBOL_STR(usb_autopm_get_interface) },
	{ 0x1ecdb81a, __VMLINUX_SYMBOL_STR(tty_standard_install) },
	{ 0xb6e19285, __VMLINUX_SYMBOL_STR(tty_port_open) },
	{ 0xd6d20c3b, __VMLINUX_SYMBOL_STR(tty_port_close) },
	{ 0x90c614ef, __VMLINUX_SYMBOL_STR(usb_autopm_get_interface_async) },
	{ 0x63d2a082, __VMLINUX_SYMBOL_STR(tty_port_hangup) },
	{ 0x8653ea87, __VMLINUX_SYMBOL_STR(tty_port_tty_wakeup) },
	{ 0x37a0cba, __VMLINUX_SYMBOL_STR(kfree) },
	{ 0xf45efc62, __VMLINUX_SYMBOL_STR(usb_put_intf) },
	{ 0x695a865d, __VMLINUX_SYMBOL_STR(tty_flip_buffer_push) },
	{ 0xabcd5edb, __VMLINUX_SYMBOL_STR(tty_insert_flip_string_fixed_flag) },
	{ 0xb2d48a2e, __VMLINUX_SYMBOL_STR(queue_work_on) },
	{ 0x2d3385d3, __VMLINUX_SYMBOL_STR(system_wq) },
	{ 0x91715312, __VMLINUX_SYMBOL_STR(sprintf) },
	{ 0xafdd2878, __VMLINUX_SYMBOL_STR(tty_port_put) },
	{ 0x7e0be157, __VMLINUX_SYMBOL_STR(usb_driver_release_interface) },
	{ 0xc2dfa496, __VMLINUX_SYMBOL_STR(usb_free_urb) },
	{ 0x63d766d, __VMLINUX_SYMBOL_STR(tty_unregister_device) },
	{ 0x731564f0, __VMLINUX_SYMBOL_STR(tty_kref_put) },
	{ 0x3ea262, __VMLINUX_SYMBOL_STR(tty_vhangup) },
	{ 0x99973b3f, __VMLINUX_SYMBOL_STR(tty_port_tty_get) },
	{ 0xe4ca3b4f, __VMLINUX_SYMBOL_STR(mutex_unlock) },
	{ 0xd33f4f47, __VMLINUX_SYMBOL_STR(device_remove_file) },
	{ 0xfd16e532, __VMLINUX_SYMBOL_STR(mutex_lock) },
	{ 0x60e556df, __VMLINUX_SYMBOL_STR(usb_free_coherent) },
	{ 0x9c0bd51f, __VMLINUX_SYMBOL_STR(_raw_spin_lock) },
	{ 0x4205ad24, __VMLINUX_SYMBOL_STR(cancel_work_sync) },
	{ 0xc95d3def, __VMLINUX_SYMBOL_STR(usb_kill_urb) },
	{ 0x676bbc0f, __VMLINUX_SYMBOL_STR(_set_bit) },
	{ 0x2a3aa678, __VMLINUX_SYMBOL_STR(_test_and_clear_bit) },
	{ 0xd697e69a, __VMLINUX_SYMBOL_STR(trace_hardirqs_on) },
	{ 0x3507a132, __VMLINUX_SYMBOL_STR(_raw_spin_lock_irq) },
	{ 0x668e40e0, __VMLINUX_SYMBOL_STR(usb_autopm_put_interface_async) },
	{ 0x4c11bf73, __VMLINUX_SYMBOL_STR(tty_port_tty_hangup) },
	{ 0xe49a8c4e, __VMLINUX_SYMBOL_STR(dev_err) },
	{ 0x3f653b74, __VMLINUX_SYMBOL_STR(usb_submit_urb) },
	{ 0x526c3a6c, __VMLINUX_SYMBOL_STR(jiffies) },
	{ 0x9d669763, __VMLINUX_SYMBOL_STR(memcpy) },
	{ 0x62fd3ede, __VMLINUX_SYMBOL_STR(usb_control_msg) },
	{ 0x2e5810c6, __VMLINUX_SYMBOL_STR(__aeabi_unwind_cpp_pr1) },
	{ 0x51d559d1, __VMLINUX_SYMBOL_STR(_raw_spin_unlock_irqrestore) },
	{ 0x598542b2, __VMLINUX_SYMBOL_STR(_raw_spin_lock_irqsave) },
	{ 0xb1ad28e0, __VMLINUX_SYMBOL_STR(__gnu_mcount_nc) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";

MODULE_ALIAS("usb:v04E2p1410d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1411d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1412d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1414d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1420d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1421d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1422d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1424d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1400d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1401d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1402d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v04E2p1403d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "17922333BF9E0AEADC7EF11");
